import re
from docx import Document
from django.conf import settings
from datetime import datetime as dt


def template_contract(filename, string, new_string):
    document = Document(f"{settings.BASE_DIR}/static/contracts/{filename}")
    for p in document.paragraphs:
        for run in p.runs:
            if run.text:
                replaced_text = re.sub(string, new_string, run.text, 999)
                if replaced_text != run.text:
                    run.text = replaced_text

    new_path = f"{settings.CONTRACT_PATH}{dt.now().strftime('%d-%m-%y-%H:%M:%S')}-{filename}"
    document.save(new_path)
    return new_path
