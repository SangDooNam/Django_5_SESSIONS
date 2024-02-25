"""Custom template tags and filters."""

from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from notes.models import NoteStore
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect

from common.models import Notes
from common.models import Votes

register = template.Library()
store = NoteStore()
notes = store.get()

@register.filter
def linked_section(section_name):
    """Return the section_name as a link."""
    link = [
        "<a href=\"",
        reverse("notes:by_section", args=[section_name]),
        "\">",
        section_name,
        "</a>"
    ]
    return "".join(link)

@register.simple_tag(takes_context=True)
def voting_link(context, note_id):
    request = context['request']
    if not request.user.is_authenticated:
        return mark_safe('You are not authorized. <a href="{}">Log in</a>'.format(reverse('login')))
    
    note = context.get('note', None)
    if note is None:
        return ''
    
    user = request.user
    user_has_voted = Votes.objects.filter(user=user,section=note.section, votes=True)
    check_if_voted = Votes.objects.get(user=user, note=note)
    voted = ['1' if check_if_voted.votes else '0']
    
    if note.section in user.voted_notes and user_has_voted[0].note_id == note.id:
        return mark_safe("<p><strong>Votes:</strong> {} You already voted this note.</p>".format(''.join(voted)))
    elif note.section in user.voted_notes and user_has_voted[0].note_id != note.id:
        return mark_safe("<p><strong>Votes:</strong> {} You already voted note number {}.".format(''.join(voted), user_has_voted[0].note_id))
    
    vote_url = reverse('notes:vote', args=[note_id])
    return mark_safe("<p><strong>Votes:</strong> {} <a href='{}'>Vote this note.</a>".format(''.join(voted),vote_url))



