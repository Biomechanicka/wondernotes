"""Напишите функцию build_note с аргументами note_text и note_name.
Она получает название и текст заметки,
а затем создает текстовый файл с этим названием и текстом."""
import os

def build_note(note_name, note_text):
    file = open("notes/"+note_name+".txt",'w',encoding="utf-8")
    file.write(note_text)
    file.close()
    print(f"Заметка \"{note_name}\" создана.")

"""Напишите функцию create_note(). Она запрашивает у пользователя название и текст заметки, 
а затем вызывает функцию build_note(note_text, note_name)."""

def create_note():
    note_name = input("Имя заметки?")
    if os.path.isfile("notes/"+note_name+".txt"):
        print(f'File {note_name} already exists.')
    note_text = input("Текст заметки?")
    build_note(note_name, note_text)

create_note()