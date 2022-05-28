import csv
from email.errors import MessageError
from jinja2 import Template, FileSystemLoader, Environment


rows = []
with open('invitations.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter=',')
    for line_number, line in enumerate(csvreader):
        if line_number == 0:
            pass
        else:
            # print(line)
            rows.append(line)

# print(rows)

file_loder = FileSystemLoader('templates')
env = Environment(loader=file_loder)
template = env.get_template('invitation.html')

for i in range(len(rows)):
    with open(f'output/{rows[i][0]}_invitation.html', 'w') as f:
        msg = template.render(line=rows[i])
        f.write(msg)
        print(f'output/{rows[i][0]}_invitation.html')
