import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    cl_text = re.sub(r'<[^>]*>', '', html_content)

    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write(cl_text)


delete_html_tags('draft.html', 'cleaned.txt')


