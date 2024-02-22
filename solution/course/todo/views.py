"""Todo views."""
from django.views.generic.edit import FormView

from common.forms import LoginForm
from todo.models import todos


class TodoDetails(FormView):
    """Todo details."""

    template_name = "todo/details.html"
    form_class = LoginForm
    # Even if we override the form_valid response, the FormView requires
    # a success_url.
    success_url = "/nothing/"

    def get_context_data(self, *args, **kwargs):
        """Get the notes in the context."""
        form = self.get_form()
        user_name = form.data.get("user_name", None)
        password = form.data.get("password", None)
        context = super().get_context_data()
        if user_name == "admin" and password == "admin":
            context["todo"] = todos[self.kwargs["todo_id"] - 1]
            context["id"] = self.kwargs["todo_id"]
            context["num_todos"] = len(todos)
        return context

    def form_valid(self, *args, **kwargs):
        """Override the default redirect behaviour."""
        return self.get(*args, **kwargs)
