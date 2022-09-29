def make_shirt(size, text):
    print(f'The shirt will be made in size {size.upper()} have the message \"{text}\".')


#Ppositional arguments 
make_shirt('large', 'The Flash is the fastest man alive!')

#Keyword arguments
make_shirt(size = 'large', text = 'The Flash is the fastest man alive!')