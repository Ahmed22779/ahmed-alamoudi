input.onButtonPressed(Button.A, function () {
    Num = Num + 2
    basic.showNumber(Num)
})
input.onButtonPressed(Button.AB, function () {
    Num = Num + 2
    basic.showNumber(Num)
})
input.onButtonPressed(Button.B, function () {
    if (Num >= 64) {
        basic.showIcon(IconNames.Diamond)
    } else {
        basic.showIcon(IconNames.Yes)
    }
})
let Num = 0
Num = 2
