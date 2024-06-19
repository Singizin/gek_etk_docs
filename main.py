from docxtpl import DocxTemplate
import os
import pandas as pd

from etsc_table import text_format


def is_red(red):
    print(f'{red=}, {type(red)=}')
    if red == 1:
        return 'С отличием'
    return 'Без отличия'


def score_text(score):
    return text_format(score)


def card_created_text(card_created: str):
    d, m, y = card_created.split('.')

    months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
              '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}

    return f'{d} {months.get(m)} {y} года'


def render_protocols():
    df = pd.read_csv('протоколы/данные/data.csv', header=0, sep=';')

    filename = os.path.abspath("протоколы/готовые/готов.docx")
    doc = DocxTemplate("протоколы/исходники/1.docx")

    context = {}

    for index, row in df.iterrows():

        number, card_created, pages, slides, time_q, red, score = row.values
        print(number, card_created, pages, slides, time_q, red, score)

        sub_context = {
            f'card_created_{number}': card_created_text(card_created),
            f'pages_{number}': str(pages),
            f'slides_{number}': str(slides),
            f'time_q_{number}': str(time_q),
            f'red_{number}': is_red(red),
            f'score_{number}': score_text(score)
        }

        if sub_context == {}:
            continue

        context.update(sub_context)

    print(context)
    doc.render(context)
    doc.save(filename)
    os.startfile(filename)


if __name__ == "__main__":
    render_protocols()
