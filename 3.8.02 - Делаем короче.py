def truncate_sentences(number, *args):
    [print(sentance[:number]) for sentance in args]


truncate_sentences(
    8,
    "Мой дядя самых честных правил,",
    "Когда не в шутку занемог,",
    "Он уважать себя заставил"
)