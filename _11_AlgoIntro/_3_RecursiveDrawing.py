def draw(number):
    def draw_downward(el):
        if el == 0:
            return 1
        line = ""
        for _ in range(el):
            line += "*"
        print(line)
        el = draw_downward(el - 1)
        return el

    def draw_upward(curr, size):
        if curr > size:
            return
        line = ""
        for _ in range(curr):
            line += "#"
        print(line)
        draw_upward(curr + 1, size)
        return

    start_upward = draw_downward(number)
    draw_upward(start_upward, number)


number_input = int(input())

draw(number_input)
