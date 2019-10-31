from test21.items import quote


class CreateItems:
    q1 = quote.Quote(text='Necessity is mother of Invention', author='ABC Albert', tags=['inspiration', 'motivation'])
    print(q1)
    print()
    print(q1.keys())

    print()
    print(q1.items())

    print()
    q3 = quote.Quote(text='Good Evening', tags=['love'])
    print(q3)

    print()
    print(q1['author'])

    print()
    print('author' in q3)   # is name field populated?

    print()
    print('author' in q3.fields)  # is author a declared field?

    q1['author'] = 'JK Ronny'  # updating the field value
    q1['author'] = 'ABCDEF'  # it replace the previous value
    print("Q1 Author:", q1)


    print()
    print(q3.get('author', 'Not Set'))
    q3_tags = q3['tags'] if q3.get('tags') else 'Tags not found.'
    print('Tags =', q3_tags)

    q3_tags = q3['tags'][0] if q3['tags'] else 'Tags not found.'
    print('Tags =', q3_tags)

    q3.setdefault('author', 'Not Found')
    print(q3)

    # q3['lala'] = 'unknow field'  # key error: unknown field in dict

    q4 = quote.Quote()
    # q4['test'] = {
    #     'b': {
    #         'xyz': [1, 2, 3],
    #     }
    # }

    k = {'b': {'xyz': [1, 2, 3]}}
    q4['test'] = k
    print(q4['test'])
    # print(q4['test']['b'])
    print(q4.get('test')['b'])
    print(q4['test']['b']['xyz'])

    t = q4['test']
    t['yy'] = {'xyz': [1, 2, 3],}
    q4['test'].update({'ds': 'dsf'})
    print(q4['test'])

    # m = [k]
    # m.append({'c': {'d': 44}})
    # print(m)

    q4['text'] = 'New Quote'
    del q4['test']
    # print('--->', q4.get('test', default='Key is Deleted'))
    print('---------')
    # if q4['test'] and q4['test']['b']:
    if q4.get('test') and q4['test']['b']:
        print(q4['test'].get('b'))
    else:
        print(q4.items())

    # q4['t'] = []
    # q4['t'] += [1, 2]
    print(q4['t'])
    # print(q4.get('t'))




