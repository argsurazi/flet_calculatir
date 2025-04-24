import flet as ft
from flet.core.types import MainAxisAlignment
'''for using "pip install flet"'''

def main(page: ft.Page):
    page.bgcolor = 'white'
    page.window.width = 320
    page.window.height = 380
    page.window.icon = 'app_icon.ico' #msin icon(assets/app_icon.ico)
    page.title = 'Calculator'
    '''creating page and setting width, height'''

    expression_plus = []
    expression_minus = []
    expression_multiply = []
    expression_devise = []
    '''sells with values by symbol'''

    def clean(e):
        text_field.value = None
        page.update()
    '''cleaning button'''

    def get_value_multiply(e):
        expression_multiply.append(int(text_field.value))
        text_field.value = ''
        page.update()
        print(expression_multiply[0])
        '''multiply button'''


    def get_value_plus(e):
        expression_plus.append(int(text_field.value))
        text_field.value = ''
        page.update()
        '''plus button'''

    def get_value_devise(e):
        expression_devise.append(int(text_field.value))
        text_field.value = ''
        page.update()
        '''devise button'''

    def get_value_minus(e):
        expression_minus.append(int(text_field.value))
        text_field.value = ''
        page.update()
        '''minus button'''


    def resulting(e):

        if expression_plus:
            expression_plus.append(int(text_field.value))
            print(bool(expression_plus))
            print(expression_plus[1])
            result = expression_plus[0] + expression_plus[1]
            text_field.value = str(result)
            expression_plus.clear()
        elif expression_minus:
            expression_minus.append(int(text_field.value))
            print(bool(expression_minus))
            print(expression_minus[1])
            result = expression_minus[0] - expression_minus[1]
            text_field.value = str(result)
            expression_minus.clear()
        elif expression_multiply:
            expression_multiply.append(int(text_field.value))
            print(bool(expression_multiply))
            print(expression_multiply[1])
            result = expression_multiply[0] * expression_multiply[1]
            text_field.value = str(result)
            expression_multiply.clear()
        elif expression_devise:
            print('1')
            expression_devise.append(int(text_field.value))
            print(bool(expression_devise))
            print(expression_devise[1])
            result = expression_devise[0] // expression_devise[1]
            text_field.value = str(result)
            print(result)
            expression_devise.clear()
            page.update()
        page.update()
    ''' "=" button '''


    def button_click(e):
        current = text_field.value
        text_field.value = current + e.control.text if current != "0" else e.control.text
        page.update()
    '''action for 1-10 buttons'''

    style = ft.ButtonStyle(
        side=ft.BorderSide(1, ft.Colors.BLACK),
        shape=ft.RoundedRectangleBorder(radius=4),
        color={
            "": ft.colors.BLACK,
            "hovered": ft.colors.WHITE
        },
        bgcolor={
            "": ft.colors.WHITE,
            "hovered": ft.colors.BLACK
        },

    )
    '''button styling + on_hover'''


    text_field = ft.TextField(value='',text_size=16, color='black', width=236, text_align=ft.TextAlign.RIGHT, hint_text='0', height=32, border_radius=4)
    '''text field creating'''
    entry = ft.Container(text_field,
    padding=10)

    '''So, on this version of calculator program dont need to use Container with button, but remove it so long('''


    button_result = ft.Container(ft.FilledButton(text='=', style=style, width=72, height=32, on_click=resulting),
                 margin=ft.margin.symmetric(0))
    button_plus = ft.Container(
        ft.FilledButton(text='+',  style=style, width=72, height=32,  on_click=get_value_plus),
        margin=ft.margin.symmetric(0))

    button_minus = ft.Container(ft.FilledButton(text='-',  style=style, width=72, height=32,  on_click=get_value_minus),
                 margin=ft.margin.symmetric(0))
    button_zero = ft.Container(ft.FilledButton(text='0', style=style, width=72, height=32, on_click=button_click), margin=ft.margin.symmetric(0))

    button_clean = ft.Container(ft.FilledButton(text='C', style=style, width=236, height=32 , on_click=clean), margin=ft.margin.symmetric(0))

    button_multiply= ft.Container(
        ft.FilledButton(text='*', style=style, width=72, height=32,  on_click=get_value_multiply),
        margin=ft.margin.symmetric(0))
    button_devise = ft.Container(
        ft.FilledButton(text='//', style=style, width=72, height=32,
                        on_click=get_value_devise),
        margin=ft.margin.symmetric(0))
    '''creating of sign buttons and 0 button '''


    buttons = [ft.Container(ft.FilledButton(text=str(i),style= style,  width=72, height=32,  on_click=button_click), margin=ft.margin.symmetric(0)) for i in range(1,10)]
    '''creating of 1-9 button'''
    page.add(
ft.Row([entry],alignment=MainAxisAlignment.CENTER, spacing=10),
        ft.Row(buttons[:3],alignment=MainAxisAlignment.CENTER, spacing=10),
        ft.Row(buttons[3:6], alignment=MainAxisAlignment.CENTER, spacing=10),
        ft.Row(buttons[6:9], alignment=MainAxisAlignment.CENTER, spacing=10),
        ft.Row([button_plus, button_zero, button_minus], alignment=MainAxisAlignment.CENTER, spacing=10),
        ft.Row([button_multiply,button_result, button_devise], alignment=MainAxisAlignment.CENTER, spacing=10),
        ft.Row([button_clean],alignment=MainAxisAlignment.CENTER, spacing=10)
             )
    '''packing elements to the page'''

if __name__ == '__main__': #start app
    ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir='assets') #connecting directory with main icon