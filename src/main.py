import flet as ft
import os
import json


def read_json_file(file_path):
    """
    Reads data from a JSON file. If the file does not exist, it creates it with {"counter": 0}.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        # If file does not exist, create it and write {"counter": 0}
        data = {"counter": 0}
        with open(file_path, "w") as file:
            json.dump(data, file)
    else:
        # If file exists, read from it
        with open(file_path, "r") as file:
            data = json.load(file)

    return data["counter"]


def update_json_file(file_path, update_value):
    """
    Updates the "counter" value in the JSON file.
    """

    # Write the updated data back to the file
    with open(file_path, "w") as file:
        json.dump({"counter": update_value}, file)


def main(page: ft.Page):
    page.title = "Counter"
    data_dir = os.getenv("FLET_APP_STORAGE_DATA") + "/data.json"

    counter = ft.Text(read_json_file(data_dir), size=50)

    def plus(n):
        def increment_click(e):
            v = read_json_file(data_dir) + n
            update_json_file(data_dir, v)
            counter.value = str(v)
            counter.update()

        return increment_click

    def re(e):
        update_json_file(data_dir, 0)
        counter.value = "0"
        counter.update()

    page.add(ft.Text(f"\n{data_dir}"))
    page.add(
        ft.Button(
            "RESET",
            on_click=re,
            style=ft.ButtonStyle(color=ft.colors.RED_50, bgcolor=ft.colors.RED),
        )
    )
    page.add(
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
                            ft.Button("+100", on_click=plus(100),style=ft.ButtonStyle(bgcolor=ft.colors.GREEN_900)),
                            ft.Button("+10"  , on_click=plus(10)  ,style=ft.ButtonStyle(bgcolor=ft.colors.GREEN_800)),
                            ft.Button("+1"    , on_click=plus(1)    ,style=ft.ButtonStyle(bgcolor=ft.colors.GREEN_700)),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            expand=True,
        )
    )


ft.app(main)
