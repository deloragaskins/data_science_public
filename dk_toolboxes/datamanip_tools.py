 def name_to_id(name):
            id=[]
            firstandlast3=[0, 1, 2,-3, -2, -1]
            for letter in firstandlast3:
                str(name)
                let=name[letter]
                id.append(ord(let))

            strings = [str(integer) for integer in id]
            a_string = "".join(strings)
            an_integer = int(a_string)

            return an_integer
