# Module by @DeBotMod
from telethon import events
from userbot import client

info = {'category': 'tools', 'pattern': '.calc', 'description': 'калькулятор обыкновенный. Вид: .calc [n+m],'
                                                                ' .calc [n-m], .calc [n^m], .calc [n*m], .calc [n/m]'}


@client.on(events.NewMessage(pattern=r'^.calc'))
async def handle_calculator(event):
    try:
        message = event.message.message
        formula = message.split()[1:]
        expression = ''.join(formula)

        if '+' in expression:
            operands = expression.split('+')
            operator = '+'
        elif '-' in expression:
            operands = expression.split('-')
            operator = '-'
        elif '*' in expression:
            operands = expression.split('*')
            operator = '*'
        elif '/' in expression:
            operands = expression.split('/')
            operator = '/'
        elif '^' in expression:
            operands = expression.split('^')
            operator = '^'
        else:
            await event.edit('Неподдерживаемая операция!')
            return

        operands = [float(operand) for operand in operands]

        result = None
        if operator == '+':
            result = sum(operands)
        elif operator == '-':
            result = operands[0] - sum(operands[1:])
        elif operator == '*':
            result = 1
            for operand in operands:
                result *= operand
        elif operator == '/':
            if 0 in operands:
                await event.edit('На ноль делить нельзя!')
                return
            result = operands[0]
            for operand in operands[1:]:
                result /= operand
        elif operator == '^':
            result = operands[0]
            for exponent in operands[1:]:
                result **= exponent
        result = round(result)
        await event.edit(f'Результат: <b>{result}</b>', parse_mode='HTML')
    except Exception as e:
        await event.edit(f'Произошла ошибка: {str(e)}')
