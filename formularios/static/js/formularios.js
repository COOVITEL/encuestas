function move(out, int, error, box1, box2, box3) {
    const query = `#${out} input[type="radio"], #${out} input[required], #${out} select[required], #${out} textarea[required]`;
    
    const camposRequeridos = document.querySelectorAll(query);
    let state = true
    let stateBox1 = false
    let stateBox2 = false
    let stateBox3 = false

    if (box1) {
        const boxes1 = document.getElementById(box1)
        const radiosBox1 = boxes1.querySelectorAll('input[type=radio]');
        radiosBox1.forEach(radio => {
            if (radio.checked) {
                stateBox1 = true;
            }
        });
    }
    if (box2) {
        const boxes2 = document.getElementById(box2)
        const radiosBox2 = boxes2.querySelectorAll('input[type=radio]');
        radiosBox2.forEach(radio => {
            if (radio.checked) {
                stateBox2 = true;
            }
        });
    }
    if (box3) {
        const boxes3 = document.getElementById(box3)
        const radiosBox3 = boxes3.querySelectorAll('input[type=radio]');
        radiosBox3.forEach(radio => {
            if (radio.checked) {
                stateBox3 = true;
            }
        });
    }

    camposRequeridos.forEach(campo => {
        if (!campo.value) {
            state = false
        }
        if (!box1) {
            stateBox1 = true
        }
        if (!box2) {
            stateBox2 = true
        }
        if (!box3) {
            stateBox3 = true
        }
    })

    if (state && stateBox1 && stateBox2 && stateBox3) {
        divOut = document.getElementById(out)
        divInt = document.getElementById(int)
        
        divOut.classList.add('outMove')
        divInt.classList.add('see')
        divInt.style.opacity = 0
        
        const addMore = () => {
            divOut.classList.add('remove')
            divOut.style.display = 'none'
            divInt.style.opacity = 1
            divInt.classList.add('intMove')
        }
        setTimeout(addMore, 500)   
    } else {
        console.log(state)
        console.log(stateBox1)
        console.log(stateBox2)
        console.log(stateBox3)
        spanError = document.getElementById(error)
        spanError.textContent = "Recuerda llenar todos los campos"
    }
}