class Garden(object):
        def plants(garden, name):
            students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph',
                        'Kincaid', 'Larry', 'another']
            flowers = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violet"}
            for i in students:
                if name not in students:
                    raise Exception("there is not student like this!")
                if i == name:
                    # print(students.index(i))
                    first = garden[students.index(i) * 2]
                    second = garden[(students.index(i) * 2) + 1]
                    third = garden[(students.index(i) * 2) + 24]
                    fourth = garden[(students.index(i) * 2) + 25]
                    return {print(flowers[first], flowers[second], flowers[third], flowers[fourth])}

        plants('VRCGVVRVCGGCCGVRGCVCGCGVVRCCCGCRRGVCGCRVVCVGCGCV', 'Bob')
        pass
