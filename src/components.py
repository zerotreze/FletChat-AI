import flet as ft


class Message:
    def __init__(self, user_name: str, text: str, user_type: str):
        self.user_name = user_name
        self.text = text
        self.user_type = user_type


class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START

        if message.user_type == 'ai':
            avatar = ft.Icon(ft.Icons.ASSISTANT, color=ft.Colors.WHITE)  
        else:
            avatar = ft.Text(self.__get_initials(message.user_name))

      
        self.controls = [
            ft.CircleAvatar(
                content=avatar,  
                color=ft.Colors.WHITE,
                bgcolor=self.__get_avatar_color(message.user_name, message.user_type),
            ),
            ft.Column(
                [
                    ft.Text(message.user_name, weight=ft.FontWeight.BOLD),
                    ft.Markdown(message.text, selectable=True, width=300),
                ],
                tight=True,
                spacing=5,
            ),
        ]

    def __get_initials(self, user_name: str) -> str:
        """
        Retorna a inicial do nome do usuário, ou 'U' se o nome estiver vazio.
        """
        return user_name[:1].capitalize() if user_name else 'U'

    def __get_avatar_color(self, user_name: str, user_type: str) -> str:
        """
        Retorna uma cor para o avatar com base no tipo de usuário ou no nome.
        """
        if user_type == 'ai':
            return ft.Colors.PURPLE

        
        colors_lookup = [
            ft.Colors.AMBER,
            ft.Colors.BLUE,
            ft.Colors.BROWN,
            ft.Colors.CYAN,
            ft.Colors.GREEN,
            ft.Colors.INDIGO,
            ft.Colors.LIME,
            ft.Colors.ORANGE,
            ft.Colors.PINK,
            ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]


        return colors_lookup[hash(user_name) % len(colors_lookup)]
