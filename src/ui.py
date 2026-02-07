"""
UI module for the Rich Todo Console Application
Handles all display, menu, prompts, and rich formatting
"""
from typing import List, Optional, Tuple
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from models import Task


class UIHandler:
    """
    Handles all UI elements including rich formatting, menus, and user prompts
    """
    def __init__(self):
        self.console = Console()

    def display_app_title(self) -> None:
        """Display the app title in a rich panel with bold text and cyan background"""
        self.console.print(
            Panel("[bold]My Todo App[/bold]", style="bold on cyan"),
            justify="center"
        )

    def display_task_summary(self, tasks: List[Task]) -> None:
        """Display live summary with total, completed, and pending task counts"""
        total = len(tasks)
        completed = sum(1 for task in tasks if task.completed)
        pending = total - completed

        summary_text = f"[bold]Total:[/bold] {total} tasks | [bold]Completed:[/bold] {completed} | [bold]Pending:[/bold] {pending}"
        self.console.print(summary_text, style="bold")
        self.console.print()  # Add blank line for spacing

    def display_menu(self) -> None:
        """Display the main menu as numbered rich list inside a bordered panel"""
        menu_text = (
            "[bold]1.[/bold] Add Task\n"
            "[bold]2.[/bold] List Tasks\n"
            "[bold]3.[/bold] Update Task\n"
            "[bold]4.[/bold] Delete Task\n"
            "[bold]5.[/bold] Mark Complete/Incomplete\n"
            "[bold]6.[/bold] Exit"
        )
        self.console.print(Panel(menu_text, title="Menu", border_style="blue"))

    def display_tasks_table(self, tasks: List[Task]) -> None:
        """Display tasks in a beautiful rich table with proper formatting"""
        if not tasks:
            self.console.print(Panel("[italic]No tasks available.[/italic]", title="Tasks", border_style="yellow"))
            return

        table = Table(title="Your Tasks", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", justify="center")
        table.add_column("Status", style="dim")
        table.add_column("Title", style="bold")
        table.add_column("Description", style="dim")

        for task in tasks:
            status = "[green]Complete[/green]" if task.completed else "[red]Incomplete[/red]"
            title = f"[bold]{task.title}[/bold]" if task.completed else task.title
            description = task.description
            if len(description) > 50:
                description = description[:47] + "..."

            table.add_row(
                str(task.id),
                status,
                title,
                description
            )

        self.console.print(table)

    def get_user_choice(self) -> Optional[int]:
        """Get and validate user menu choice"""
        try:
            choice = Prompt.ask("[bold blue]Enter your choice[/bold blue]", default="0")
            return int(choice)
        except ValueError:
            self.show_error("Please enter a valid number.")
            return None

    def get_task_input(self) -> Tuple[str, str]:
        """Get task title and description from user with validation"""
        title = Prompt.ask("[bold green]Enter task title[/bold green]").strip()

        # Validate title is not empty
        while not title:
            self.show_error("Title cannot be empty. Please enter a valid title.")
            title = Prompt.ask("[bold green]Enter task title[/bold green]").strip()

        description = Prompt.ask("[bold green]Enter task description (optional)[/bold green]", default="").strip()
        return title, description

    def show_error(self, message: str) -> None:
        """Display error message in red"""
        self.console.print(f"[bold red]Error:[/bold red] {message}")

    def show_success(self, message: str) -> None:
        """Display success message in green"""
        self.console.print(f"[bold green]Success:[/bold green] {message}")

    def show_info(self, message: str) -> None:
        """Display info message in yellow"""
        self.console.print(f"[bold yellow]Info:[/bold yellow] {message}")

    def get_task_id(self) -> Optional[int]:
        """Get task ID from user with validation"""
        try:
            task_id_str = Prompt.ask("[bold blue]Enter task ID[/bold blue]").strip()
            task_id = int(task_id_str)
            if task_id <= 0:
                self.show_error("Task ID must be a positive number.")
                return None
            return task_id
        except ValueError:
            self.show_error("Please enter a valid number for task ID.")
            return None

    def confirm_delete(self, task: Task) -> bool:
        """Show confirmation prompt for task deletion"""
        return Confirm.ask(f"[bold red]Are you sure you want to delete task {task.id}: '{task.title}'?[/bold red]")

    def get_update_options(self) -> str:
        """Get update option from user (title/description/both/cancel)"""
        options_text = (
            "[bold]1.[/bold] Update title\n"
            "[bold]2.[/bold] Update description\n"
            "[bold]3.[/bold] Update both title and description\n"
            "[bold]4.[/bold] Cancel"
        )
        self.console.print(Panel(options_text, title="Update Options", border_style="blue"))

        choice = Prompt.ask("[bold blue]Choose an option[/bold blue]", choices=["1", "2", "3", "4"], default="4")
        return choice

    def show_exit_message(self) -> None:
        """Display exit message"""
        self.console.print("[bold green]Goodbye![/bold green]")