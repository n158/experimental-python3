if __name__=='__main__':
    def cmp(a, b):
        return (a > b) - (a < b)

    print(''.join(
        '%(pre)s%(num)s %(bot)s on the wall, %(nul)s %(bot)s,\n%(tak)s\n' %
        (lambda c, b:{'pre':['', '%s %s on the wall.\n\n' % (c, b)][abs(cmp(c, 'Ninety-nine'))],
                      'num':c, 'nul':c.lower(),
                      'bot':b,
                      'tak':['Go to the store and buy some more... Ninety-nine %s.' % b,
                             'Take one down, pass it around,'][abs(cmp(x, 0))]})(
            (lambda x, o:[(['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty',
                            'Ninety'][x // 10 - 2] + '-' + o.lower())
             .replace('-no more', ''), o][int(x < 20)])(
                x, ['No more', 'One', 'Two', 'Three', 'Four',
                    'Five', 'Six', 'Seven', 'Eight', 'Nine',
                    'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                    'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
                [[x, x % 10][int(x >= 20)]]), 'bottle%s of beer' % ['', 's'][abs(cmp(x, 1))])
        for x in range(99, -1, -1)))

"""
Ninety-nine bottles of beer on the wall, ninety-nine bottles of beer,
Take one down, pass it around,
Ninety-eight bottles of beer on the wall.

Ninety-eight bottles of beer on the wall, ninety-eight bottles of beer,
Take one down, pass it around,
Ninety-seven bottles of beer on the wall.

Ninety-seven bottles of beer on the wall, ninety-seven bottles of beer,
Take one down, pass it around,
Ninety-six bottles of beer on the wall.

Ninety-six bottles of beer on the wall, ninety-six bottles of beer,
Take one down, pass it around,
Ninety-five bottles of beer on the wall.

Ninety-five bottles of beer on the wall, ninety-five bottles of beer,
Take one down, pass it around,
Ninety-four bottles of beer on the wall.

Ninety-four bottles of beer on the wall, ninety-four bottles of beer,
Take one down, pass it around,
Ninety-three bottles of beer on the wall.

Ninety-three bottles of beer on the wall, ninety-three bottles of beer,
Take one down, pass it around,
Ninety-two bottles of beer on the wall.

Ninety-two bottles of beer on the wall, ninety-two bottles of beer,
Take one down, pass it around,
Ninety-one bottles of beer on the wall.

Ninety-one bottles of beer on the wall, ninety-one bottles of beer,
Take one down, pass it around,
Ninety bottles of beer on the wall.

Ninety bottles of beer on the wall, ninety bottles of beer,
Take one down, pass it around,
Eighty-nine bottles of beer on the wall.

Eighty-nine bottles of beer on the wall, eighty-nine bottles of beer,
Take one down, pass it around,
Eighty-eight bottles of beer on the wall.

Eighty-eight bottles of beer on the wall, eighty-eight bottles of beer,
Take one down, pass it around,
Eighty-seven bottles of beer on the wall.

Eighty-seven bottles of beer on the wall, eighty-seven bottles of beer,
Take one down, pass it around,
Eighty-six bottles of beer on the wall.

Eighty-six bottles of beer on the wall, eighty-six bottles of beer,
Take one down, pass it around,
Eighty-five bottles of beer on the wall.

Eighty-five bottles of beer on the wall, eighty-five bottles of beer,
Take one down, pass it around,
Eighty-four bottles of beer on the wall.

Eighty-four bottles of beer on the wall, eighty-four bottles of beer,
Take one down, pass it around,
Eighty-three bottles of beer on the wall.

Eighty-three bottles of beer on the wall, eighty-three bottles of beer,
Take one down, pass it around,
Eighty-two bottles of beer on the wall.

Eighty-two bottles of beer on the wall, eighty-two bottles of beer,
Take one down, pass it around,
Eighty-one bottles of beer on the wall.

Eighty-one bottles of beer on the wall, eighty-one bottles of beer,
Take one down, pass it around,
Eighty bottles of beer on the wall.

Eighty bottles of beer on the wall, eighty bottles of beer,
Take one down, pass it around,
Seventy-nine bottles of beer on the wall.

Seventy-nine bottles of beer on the wall, seventy-nine bottles of beer,
Take one down, pass it around,
Seventy-eight bottles of beer on the wall.

Seventy-eight bottles of beer on the wall, seventy-eight bottles of beer,
Take one down, pass it around,
Seventy-seven bottles of beer on the wall.

Seventy-seven bottles of beer on the wall, seventy-seven bottles of beer,
Take one down, pass it around,
Seventy-six bottles of beer on the wall.

Seventy-six bottles of beer on the wall, seventy-six bottles of beer,
Take one down, pass it around,
Seventy-five bottles of beer on the wall.

Seventy-five bottles of beer on the wall, seventy-five bottles of beer,
Take one down, pass it around,
Seventy-four bottles of beer on the wall.

Seventy-four bottles of beer on the wall, seventy-four bottles of beer,
Take one down, pass it around,
Seventy-three bottles of beer on the wall.

Seventy-three bottles of beer on the wall, seventy-three bottles of beer,
Take one down, pass it around,
Seventy-two bottles of beer on the wall.

Seventy-two bottles of beer on the wall, seventy-two bottles of beer,
Take one down, pass it around,
Seventy-one bottles of beer on the wall.

Seventy-one bottles of beer on the wall, seventy-one bottles of beer,
Take one down, pass it around,
Seventy bottles of beer on the wall.

Seventy bottles of beer on the wall, seventy bottles of beer,
Take one down, pass it around,
Sixty-nine bottles of beer on the wall.

Sixty-nine bottles of beer on the wall, sixty-nine bottles of beer,
Take one down, pass it around,
Sixty-eight bottles of beer on the wall.

Sixty-eight bottles of beer on the wall, sixty-eight bottles of beer,
Take one down, pass it around,
Sixty-seven bottles of beer on the wall.

Sixty-seven bottles of beer on the wall, sixty-seven bottles of beer,
Take one down, pass it around,
Sixty-six bottles of beer on the wall.

Sixty-six bottles of beer on the wall, sixty-six bottles of beer,
Take one down, pass it around,
Sixty-five bottles of beer on the wall.

Sixty-five bottles of beer on the wall, sixty-five bottles of beer,
Take one down, pass it around,
Sixty-four bottles of beer on the wall.

Sixty-four bottles of beer on the wall, sixty-four bottles of beer,
Take one down, pass it around,
Sixty-three bottles of beer on the wall.

Sixty-three bottles of beer on the wall, sixty-three bottles of beer,
Take one down, pass it around,
Sixty-two bottles of beer on the wall.

Sixty-two bottles of beer on the wall, sixty-two bottles of beer,
Take one down, pass it around,
Sixty-one bottles of beer on the wall.

Sixty-one bottles of beer on the wall, sixty-one bottles of beer,
Take one down, pass it around,
Sixty bottles of beer on the wall.

Sixty bottles of beer on the wall, sixty bottles of beer,
Take one down, pass it around,
Fifty-nine bottles of beer on the wall.

Fifty-nine bottles of beer on the wall, fifty-nine bottles of beer,
Take one down, pass it around,
Fifty-eight bottles of beer on the wall.

Fifty-eight bottles of beer on the wall, fifty-eight bottles of beer,
Take one down, pass it around,
Fifty-seven bottles of beer on the wall.

Fifty-seven bottles of beer on the wall, fifty-seven bottles of beer,
Take one down, pass it around,
Fifty-six bottles of beer on the wall.

Fifty-six bottles of beer on the wall, fifty-six bottles of beer,
Take one down, pass it around,
Fifty-five bottles of beer on the wall.

Fifty-five bottles of beer on the wall, fifty-five bottles of beer,
Take one down, pass it around,
Fifty-four bottles of beer on the wall.

Fifty-four bottles of beer on the wall, fifty-four bottles of beer,
Take one down, pass it around,
Fifty-three bottles of beer on the wall.

Fifty-three bottles of beer on the wall, fifty-three bottles of beer,
Take one down, pass it around,
Fifty-two bottles of beer on the wall.

Fifty-two bottles of beer on the wall, fifty-two bottles of beer,
Take one down, pass it around,
Fifty-one bottles of beer on the wall.

Fifty-one bottles of beer on the wall, fifty-one bottles of beer,
Take one down, pass it around,
Fifty bottles of beer on the wall.

Fifty bottles of beer on the wall, fifty bottles of beer,
Take one down, pass it around,
Forty-nine bottles of beer on the wall.

Forty-nine bottles of beer on the wall, forty-nine bottles of beer,
Take one down, pass it around,
Forty-eight bottles of beer on the wall.

Forty-eight bottles of beer on the wall, forty-eight bottles of beer,
Take one down, pass it around,
Forty-seven bottles of beer on the wall.

Forty-seven bottles of beer on the wall, forty-seven bottles of beer,
Take one down, pass it around,
Forty-six bottles of beer on the wall.

Forty-six bottles of beer on the wall, forty-six bottles of beer,
Take one down, pass it around,
Forty-five bottles of beer on the wall.

Forty-five bottles of beer on the wall, forty-five bottles of beer,
Take one down, pass it around,
Forty-four bottles of beer on the wall.

Forty-four bottles of beer on the wall, forty-four bottles of beer,
Take one down, pass it around,
Forty-three bottles of beer on the wall.

Forty-three bottles of beer on the wall, forty-three bottles of beer,
Take one down, pass it around,
Forty-two bottles of beer on the wall.

Forty-two bottles of beer on the wall, forty-two bottles of beer,
Take one down, pass it around,
Forty-one bottles of beer on the wall.

Forty-one bottles of beer on the wall, forty-one bottles of beer,
Take one down, pass it around,
Forty bottles of beer on the wall.

Forty bottles of beer on the wall, forty bottles of beer,
Take one down, pass it around,
Thirty-nine bottles of beer on the wall.

Thirty-nine bottles of beer on the wall, thirty-nine bottles of beer,
Take one down, pass it around,
Thirty-eight bottles of beer on the wall.

Thirty-eight bottles of beer on the wall, thirty-eight bottles of beer,
Take one down, pass it around,
Thirty-seven bottles of beer on the wall.

Thirty-seven bottles of beer on the wall, thirty-seven bottles of beer,
Take one down, pass it around,
Thirty-six bottles of beer on the wall.

Thirty-six bottles of beer on the wall, thirty-six bottles of beer,
Take one down, pass it around,
Thirty-five bottles of beer on the wall.

Thirty-five bottles of beer on the wall, thirty-five bottles of beer,
Take one down, pass it around,
Thirty-four bottles of beer on the wall.

Thirty-four bottles of beer on the wall, thirty-four bottles of beer,
Take one down, pass it around,
Thirty-three bottles of beer on the wall.

Thirty-three bottles of beer on the wall, thirty-three bottles of beer,
Take one down, pass it around,
Thirty-two bottles of beer on the wall.

Thirty-two bottles of beer on the wall, thirty-two bottles of beer,
Take one down, pass it around,
Thirty-one bottles of beer on the wall.

Thirty-one bottles of beer on the wall, thirty-one bottles of beer,
Take one down, pass it around,
Thirty bottles of beer on the wall.

Thirty bottles of beer on the wall, thirty bottles of beer,
Take one down, pass it around,
Twenty-nine bottles of beer on the wall.

Twenty-nine bottles of beer on the wall, twenty-nine bottles of beer,
Take one down, pass it around,
Twenty-eight bottles of beer on the wall.

Twenty-eight bottles of beer on the wall, twenty-eight bottles of beer,
Take one down, pass it around,
Twenty-seven bottles of beer on the wall.

Twenty-seven bottles of beer on the wall, twenty-seven bottles of beer,
Take one down, pass it around,
Twenty-six bottles of beer on the wall.

Twenty-six bottles of beer on the wall, twenty-six bottles of beer,
Take one down, pass it around,
Twenty-five bottles of beer on the wall.

Twenty-five bottles of beer on the wall, twenty-five bottles of beer,
Take one down, pass it around,
Twenty-four bottles of beer on the wall.

Twenty-four bottles of beer on the wall, twenty-four bottles of beer,
Take one down, pass it around,
Twenty-three bottles of beer on the wall.

Twenty-three bottles of beer on the wall, twenty-three bottles of beer,
Take one down, pass it around,
Twenty-two bottles of beer on the wall.

Twenty-two bottles of beer on the wall, twenty-two bottles of beer,
Take one down, pass it around,
Twenty-one bottles of beer on the wall.

Twenty-one bottles of beer on the wall, twenty-one bottles of beer,
Take one down, pass it around,
Twenty bottles of beer on the wall.

Twenty bottles of beer on the wall, twenty bottles of beer,
Take one down, pass it around,
Nineteen bottles of beer on the wall.

Nineteen bottles of beer on the wall, nineteen bottles of beer,
Take one down, pass it around,
Eighteen bottles of beer on the wall.

Eighteen bottles of beer on the wall, eighteen bottles of beer,
Take one down, pass it around,
Seventeen bottles of beer on the wall.

Seventeen bottles of beer on the wall, seventeen bottles of beer,
Take one down, pass it around,
Sixteen bottles of beer on the wall.

Sixteen bottles of beer on the wall, sixteen bottles of beer,
Take one down, pass it around,
Fifteen bottles of beer on the wall.

Fifteen bottles of beer on the wall, fifteen bottles of beer,
Take one down, pass it around,
Fourteen bottles of beer on the wall.

Fourteen bottles of beer on the wall, fourteen bottles of beer,
Take one down, pass it around,
Thirteen bottles of beer on the wall.

Thirteen bottles of beer on the wall, thirteen bottles of beer,
Take one down, pass it around,
Twelve bottles of beer on the wall.

Twelve bottles of beer on the wall, twelve bottles of beer,
Take one down, pass it around,
Eleven bottles of beer on the wall.

Eleven bottles of beer on the wall, eleven bottles of beer,
Take one down, pass it around,
Ten bottles of beer on the wall.

Ten bottles of beer on the wall, ten bottles of beer,
Take one down, pass it around,
Nine bottles of beer on the wall.

Nine bottles of beer on the wall, nine bottles of beer,
Take one down, pass it around,
Eight bottles of beer on the wall.

Eight bottles of beer on the wall, eight bottles of beer,
Take one down, pass it around,
Seven bottles of beer on the wall.

Seven bottles of beer on the wall, seven bottles of beer,
Take one down, pass it around,
Six bottles of beer on the wall.

Six bottles of beer on the wall, six bottles of beer,
Take one down, pass it around,
Five bottles of beer on the wall.

Five bottles of beer on the wall, five bottles of beer,
Take one down, pass it around,
Four bottles of beer on the wall.

Four bottles of beer on the wall, four bottles of beer,
Take one down, pass it around,
Three bottles of beer on the wall.

Three bottles of beer on the wall, three bottles of beer,
Take one down, pass it around,
Two bottles of beer on the wall.

Two bottles of beer on the wall, two bottles of beer,
Take one down, pass it around,
One bottle of beer on the wall.

One bottle of beer on the wall, one bottle of beer,
Take one down, pass it around,
No more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer,
Go to the store and buy some more... Ninety-nine bottles of beer.
"""
