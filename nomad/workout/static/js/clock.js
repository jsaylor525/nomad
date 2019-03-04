class Time {
  constructor() {
    this.milliseconds = Date.now()
  }

  get ms() {
    return milliseconds % 1000;
  }

  get s() {
    return Math.floor(milliseconds / 1000) % 60;
  }

  get m() {
    return Math.floor(milliseconds / 1000 / 60) % 60;
  }

  get h() {
    return Math.floor(milliseconds / 1000 / 60 / 60);
  }

  get rawTime() {
    return milliseconds;
  }
  
  get millisecondDigits() {
    return [this.ms % 10, Math.floor(this.ms / 10) % 10, Math.floor(this.ms / 100) ];
  }

  get millisecondDigit(digit) {
    return this.millisecondDigits[digits];
  }
  
  get secondDigits() {
    return [this.s % 10, Math.floor(this.s / 10) % 10];
  }

  get secondDigit(digit) {
    return this.secondDigits[digits];
  }
  
  get minutesDigits() {
    return [this.m % 10, Math.floor(this.m / 10) % 10];
  }

  get minutesDigit(digit) {
    return this.minutesDigits[digits];
  }

  minus(time) {
    return (this.milliseconds -= time.rawTime)
  }
}

var digitSegments = [
  [1, 2, 3, 4, 5, 6],
  [2, 3],
  [1, 2, 7, 5, 4],
  [1, 2, 7, 3, 4],
  [6, 7, 2, 3],
  [1, 6, 7, 3, 4],
  [1, 6, 5, 4, 3, 7],
  [1, 2, 3],
  [1, 2, 3, 4, 5, 6, 7],
  [1, 2, 7, 3, 6]
];

class ClockDigit {
  constructor(digit) {
    this.digit = digit;
  }

  setNumber(value, on = 1) {
    var current = parseInt(digit.getAttribute('data-value'));

    // only switch if number has changed or wasn't set
    if (!isNaN(current) && current != value) {
      // unset previous number
      digitSegments[current].forEach(function (digitSegment, index) {
        setTimeout(function () {
          digit[digitSegment - 1].classList.remove('on');
        }, index * 45)
      });
    }

    if (isNaN(current) || current != number) {
      // set new number after
      setTimeout(function () {
        digitSegments[number].forEach(function (digitSegment, index) {
          setTimeout(function () {
            digit[digitSegment - 1].classList.add('on');
          }, index * 45)
        });
      }, 250);
      digit.setAttribute('data-value', number);
    }
  }

  clearNumber() {
    setNumber(0, on);
  }
}

class WodClock {
  constructor() {
    this._hours = document.querySelectorAll('.hours');
    this._minutes = document.querySelectorAll('.minutes');
    this._seconds = document.querySelectorAll('.seconds');
    this._milliseconds = document.querySelectorAll('.milliseconds');
    this._digit = {
      "hours": [],
      "minutes": [],
      "seconds": [],
      "milliseconds": [],
    }
    this._hours.forEach(digit => this._digit["hours"].push(new ClockDigit(digit)));
    this._minutes.forEach(digit => this._digit["minutes"].push(new ClockDigit(digit)));
    this._seconds.forEach(digit => this._digit["seconds"].push(new ClockDigit(digit)));
    this._milliseconds.forEach(digit => this._digit["milliseconds"].push(new ClockDigit(digit)));
    this._startTime = null;
    this._curretTime = null;
    this._clockEnable = false;
  }

  startClock() {
    this._clockEnable = true;
    this._startTime = new Time();
    setInterval(() => {
      if (this._clockEnable) {
        var currentTime = new Time();
        currentTime.minus(this._startTime);

        // this._digit["hours"][0].setNumber(currentTime.millisecondDigit[0], 1);
        // this._digit["hours"][1].setNumber(currentTime.millisecondDigit[1], 1);
        // this._digit["minutes"][0].setNumber(Math.floor(minutes / 10), 1);
        // this._digit["minutes"][1].setNumber(minutes % 10, 1);
        this._digit["seconds"][0].setNumber(Math.floor(seconds / 10), 1);
        this._digit["seconds"][1].setNumber(seconds % 10, 1);
        // this._digit["milliseconds"][0].setNumber(Math.floor(millisecond / 100), 1);
        // this._digit["milliseconds"][1].setNumber(Math.floor(millisecond / 10), 1);
        // this._digit["milliseconds"][3].setNumber(seconds % 10, 1);
      }
    }, Math.floor(Math.random() * 10));
  }

  stopClock() {
    this.clockEnable = false;
    clearInterval(this.updateClock);
    clearClock();
  }

}

$(document).ready(function () {
  var controls = {
    startTimer: $("#start-btn"),
    stopTimer: $("#stop-btn"),
  }

  var clock = new WodClock();

  function archiveClock(time) {
    var entry = document.createElement('li');
    entry.appendChild(document.createTextNode(time))
    var clockList = document.getElementById('clock-list')
    clockList.appendChild(entry)
  }

  controls.startTimer.click(() => clock.startClock());
  controls.stopTimer.click(() => clock.stopClock());

});