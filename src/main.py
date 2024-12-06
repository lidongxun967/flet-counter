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
        with open(file_path, 'w') as file:
            json.dump(data, file)
    else:
        # If file exists, read from it
        with open(file_path, 'r') as file:
            data = json.load(file)
    
    return data["counter"]

def update_json_file(file_path, update_value):
    """
    Updates the "counter" value in the JSON file.
    """
    
    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump({"counter": update_value}, file)


def main(page: ft.Page):
    page.title = "Counter"
    data_dir = os.getenv("FLET_APP_STORAGE_DATA")+"/data.json"
    
    counter = ft.Text(read_json_file(data_dir), size=50)

    def increment_click(e):
        update_json_file(data_dir,read_json_file(data_dir)+1)
        counter.value=str(read_json_file(data_dir))
        counter.update()
    
    def re(e):
        update_json_file(data_dir,0)
        counter.value="0"
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(ft.Text(f"\n{data_dir}"))
    page.add(ft.Button(
        "RESET",
        on_click=re
    ))
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
