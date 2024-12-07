import flet as ft
import os
import json_tool


def main(page: ft.Page):
    page.title = "Counter"
    data_dir = os.getenv("FLET_APP_STORAGE_DATA") + "/data.json"
    v = json_tool.read_json_file(data_dir)

    def open_dlg(e):
        def reset_click(e):
            json_tool.reset_json_file(data_dir)
            page.window.destroy()
        
        dlg = ft.AlertDialog(
            title=ft.Text("Debug Info"),
            content=ft.Column(
                [
                    ft.Text("Data file url: "),
                    ft.TextField(
                        data_dir,
                        multiline=True,
                        read_only=True,
                    ),
                    ft.Text("Data file content: "),
                    ft.TextField(
                        json_tool.read_json_file(data_dir),
                        multiline=True,
                        read_only=True,
                    ),ft.Text("完全重置"),
                    ft.Button("确定", on_click=reset_click,style=ft.ButtonStyle(text_style=ft.TextStyle(size=30),shape=ft.RoundedRectangleBorder(radius=10),bgcolor=ft.Colors.RED, color=ft.Colors.WHITE)),
                ],
                height=300,
            ),
        )
        page.open(dlg)

    def calc(c, n):

        # 静态
        def increment_click(e):
            v = json_tool.read_json_file(data_dir)
            if c == "+":
                v["counter"] += n
            elif c == "*":
                v["counter"] *= n
            elif c == "/":
                v["counter"] //= n
            elif c == "-":
                v["counter"] -= n
            json_tool.update_json_file(data_dir, v)
            counter.value = str(v["counter"])
            counter.update()

        return increment_click

    def dcalc(c, n):
        # 对于固定增加值的点击事件
        def increment_click(e):
            v = json_tool.read_json_file(data_dir)
            if c.value == "+":
                v["counter"] += int(n.value)
            elif c.value == "*":
                v["counter"] *= int(n.value)
            elif c.value == "/":
                v["counter"] //= int(n.value)
            elif c.value == "-":
                v["counter"] -= int(n.value)
            v["n"] = int(n.value)
            v["o"] = c.value
            json_tool.update_json_file(data_dir, v)
            counter.value = str(v["counter"])
            counter.update()

        return increment_click

    def iptplus(iptn):
        # 对于动态增加值的点击事件
        def increment_click(e):
            v = json_tool.read_json_file(data_dir)
            v["counter"] += int(iptn.value)
            v["plusn"] = int(iptn.value)
            json_tool.update_json_file(data_dir, v)
            counter.value = str(v["counter"])
            counter.update()

        return increment_click

    def re(e):
        # 重置按钮的点击事件
        v = json_tool.read_json_file(data_dir)
        v["counter"] = 0
        json_tool.update_json_file(data_dir, v)
        counter.value = "0"
        counter.update()

    # 预注册组件
    itt = ft.Dropdown(
        width=50,
        value=v["o"],
        options=[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("*"),
            ft.dropdown.Option("/"),
        ],
    )
    it = ft.TextField(
        label="",
        value=v["n"],
        width=100,
        input_filter=ft.InputFilter(
            allow=True, regex_string=r"^[0-9]*$", replacement_string=""
        ),
    )
    counter = ft.Text(json_tool.read_json_file(data_dir)["counter"], size=100)

    # 页面构建
    page.add(
        ft.ElevatedButton(
            "调试",
            on_click=open_dlg,
            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
        ),
        ft.SafeArea(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                counter,
                                alignment=ft.alignment.center,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.Button(
                                "+100",
                                on_click=calc("+", 100),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_900),
                            ),
                            ft.Button(
                                "+10",
                                on_click=calc("+", 10),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_800),
                            ),
                            ft.Button(
                                "+1",
                                on_click=calc("+", 1),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [itt, it, ft.Button("=", on_click=dcalc(itt, it))],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            expand=True,
        ),
        ft.Button(
            "重置",
            on_click=re,
            style=ft.ButtonStyle(color=ft.Colors.RED_50, bgcolor=ft.Colors.RED),
        ),
    )


ft.app(main)
