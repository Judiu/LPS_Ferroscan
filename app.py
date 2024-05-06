import os
import json
import flet as ft

def ventana(page: ft.page):
    page.title = "Ventana"
    page.vertical_alignment = ft.Alignment.CENTER
    return "Ventana creada"

if __name__ == '__main__':
    ventana()