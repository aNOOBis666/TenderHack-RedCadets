const checkbox = document.querySelector('#enableSecond'),
    checkboxLabel = document.querySelector('.enableSecondClass'),
    botRight = document.querySelector('.bot__right'),
    botRightLimit = document.querySelector('#limit2'),
    botRightTime = document.querySelector('#time2'),
    botLeftLimit = document.querySelector('#limit'),
    botLeftTime = document.querySelector('#time'),
    allRightRadios = document.querySelectorAll('#rightRadios input'),
    allLeftRadios = document.querySelectorAll('#leftRadios input'),
    leftRadioInstant = document.querySelector('#Instant'),
    leftRadioExact = document.querySelector('#Exact'),
    leftRadioMinutes = document.querySelector('#Minutes'),
    rightRadioInstant = document.querySelector('#Instant2'),
    rightRadioExact = document.querySelector('#Exact2'),
    rightRadioMinutes = document.querySelector('#Minutes2'),
    leftDropdown = document.querySelector('#INN'),
    rightDropdown = document.querySelector('#INN2'),
    modal = document.querySelector('#modal'),
    profile = document.querySelector('#profile'),
    modalClose = document.querySelector('#modalClose'),
    leftTradeMode = document.querySelector('#Mode'),
    rightTradeMode = document.querySelector('#Mode2'),
    play = document.querySelector('#play'),
    pause = document.querySelector('#pause'),
    stop = document.querySelector('#stop'),
    showCaseBtn = document.querySelector('.showCaseBtn');

function enableDisableFields() {
    if (checkbox.checked) {
        botRightLimit.disabled = false;
        botRightTime.disabled = false;
        allRightRadios.forEach((btn) => {
            btn.disabled = false;
        });
        rightDropdown.disabled = false;
        rightTradeMode.disabled = false;
        botLeftTime.disabled = true;
        allLeftRadios.forEach(item => {
            item.disabled = true;
        });
        leftTradeMode.disabled = true;
    } else {
        botRightLimit.disabled = true;
        botRightTime.disabled = true;
        allRightRadios.forEach((btn) => {
            btn.disabled = true;
        });
        rightDropdown.disabled = true;
        rightTradeMode.disabled = true;
        botLeftTime.disabled = false;
        allLeftRadios.forEach(item => {
            item.disabled = false;
        })
        leftTradeMode.disabled = false;
    }
}

function toggleRightForm() {
    showCaseBtn.addEventListener('click', () => {
        checkbox.classList.toggle('btnHide');
        botRight.classList.toggle('btnHide');
        checkboxLabel.classList.toggle('btnHide');
    });
}

toggleRightForm();

function changeLeftInputType() {
    leftRadioInstant.addEventListener('change', () => {
        botLeftTime.disabled = true;
        botLeftTime.placeholder = 'Сейчас';
    });
    leftRadioExact.addEventListener('change', () => {
        botLeftTime.disabled = false;
        botLeftTime.type = 'datetime-local';
    });
    leftRadioMinutes.addEventListener('change', () => {
        botLeftTime.disabled = false;
        botLeftTime.type = 'number';
        botLeftTime.placeholder = 'Время подачи предложения (мин)';
    });
}

function changeRightInputType() {
    rightRadioInstant.addEventListener('change', () => {
        botRightTime.disabled = true;
        botRightTime.placeholder = 'Сейчас';
    });
    rightRadioExact.addEventListener('change', () => {
        botRightTime.disabled = false;
        botRightTime.type = 'datetime-local';
    });
    rightRadioMinutes.addEventListener('change', () => {
        botRightTime.disabled = false;
        botRightTime.type = 'number';
        botRightTime.placeholder = 'Время подачи предложения (мин)';
    });
}

changeLeftInputType();
changeRightInputType();

checkbox.addEventListener('change', () => {
    botRight.classList.toggle('hide');
    enableDisableFields();
});

function openModal() {
    profile.addEventListener('click', () => {
        modal.classList.remove('modalHide');
        modal.classList.add('modalShow');
    });
}

function closeModal() {
    modalClose.addEventListener('click', () => {
        modal.classList.add('modalHide');
    });
}

openModal();
closeModal();

// fetch('http://127.0.0.1:8000/dealsList/')
//     .then(res => res.json())
//     .then(json => console.log(json))

const deal = {
    id_deal: 23,
    name_deal: 'First name',
    description_deal: 'Description',
    date_deal: 'Monday',
    owner_id: 12,
    first_place_id: 10,
    second_place_id: 9,
    status_deal: 'in progress',
    start_price: 'thousand',
}

function makeGet() {
    const request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:8000/dealsList/');
    request.send();
    request.onload = function () {
        let response_obj = request.response;
        console.log(response_obj.description_deal);
    }
}

makeGet();

function showOtherBtn() {
    play.addEventListener('click', () => {
        pause.classList.remove('btnHide');
        stop.classList.remove('btnHide');
        play.style.backgroundColor = 'green';
        pause.style.backgroundColor = 'grey';
    });
    stop.addEventListener('click', () => {
        pause.classList.add('btnHide');
        stop.classList.add('btnHide');
    });
    pause.addEventListener('click', () => {
        pause.style.backgroundColor = 'green';
        play.style.backgroundColor = 'grey';
    });
}


showOtherBtn();

const deadline = '2022-04-18';

function getTimeRemaining(endtime) {
    const t = Date.parse(endtime) - Date.parse(new Date()),
        // days = Math.floor(t / (1000 * 60 * 60 * 24)),
        hours = Math.floor((t / (1000 * 60 * 60) % 24)),
        minutes = Math.floor((t / 1000 / 60) % 60),
        seconds = Math.floor((t / 1000) % 60);
    return {
        'total': t,
        // 'days': days, 
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    };
}

function getZero(num) {
    if (num >= 0 && num < 10) {
        return `0${num}`;
    } else {
        return num;
    }
}

function setClock(parentSelector, endtime) {
    const timer = document.querySelector(parentSelector),
        // days = timer.querySelector('#days'), // Вычисление дней
        hours = timer.querySelector('#hours'),
        minutes = timer.querySelector('#minutes'),
        seconds = timer.querySelector('#seconds'),
        timeInterval = setInterval(reloadTimer, 1000);

    reloadTimer();

    function reloadTimer() {
        const t = getTimeRemaining(endtime);
        // days.innerHTML = getZero(t.days); // Счетчик дней
        hours.innerHTML = getZero(t.hours);
        minutes.innerHTML = getZero(t.minutes);
        seconds.innerHTML = getZero(t.seconds);

        if (t.total <= 0) {
            clearInterval(timeInterval);
        }
    }
}

setClock('.timer', deadline);

function addFormulaCount() {
    botLeftLimit.addEventListener('input', () => {
        const request = new XMLHttpRequest();
        request.open('GET', url)
        request.send();

        request.addEventListener('readystatechange', () => {
            if (request.status === 200) {
                const data = JSON.parse(request.response);
                botRightLimit = (+botLeftLimit + 50).toFixed(2); //Допилить функцию
            }
        });
    });
}



addFormulaCount();