function generateMatrices() {

    const rows = parseInt(document.getElementById("rows").value);
    const cols = parseInt(document.getElementById("cols").value);

    createMatrix("matrixA", rows, cols);
    createMatrix("matrixB", rows, cols);

    document.getElementById("result").innerHTML = "";

    hideNote();
}


function createMatrix(id, rows, cols) {

    const container = document.getElementById(id);

    container.innerHTML = "";

    const grid = document.createElement("div");
    grid.className = "matrix-grid";
    grid.style.gridTemplateColumns = `repeat(${cols}, 65px)`;

    for (let i = 0; i < rows; i++) {

        for (let j = 0; j < cols; j++) {

            const input = document.createElement("input");

            input.type = "number";
            input.value = "0";

            grid.appendChild(input);
        }
    }

    container.appendChild(grid);
}


function getMatrix(id, rows, cols) {

    const inputs = document
        .getElementById(id)
        .querySelectorAll("input");

    let matrix = [];
    let index = 0;

    for (let i = 0; i < rows; i++) {

        let row = [];

        for (let j = 0; j < cols; j++) {

            row.push(Number(inputs[index].value));
            index++;
        }

        matrix.push(row);
    }

    return matrix;
}


/* ---------- NEW FUNCTIONS ---------- */

function showNote() {

    document.getElementById("operationNote").style.display = "block";

    document.getElementById("matrixBCard")
        .classList.add("disabled-card");
}


function hideNote() {

    document.getElementById("operationNote").style.display = "none";

    document.getElementById("matrixBCard")
        .classList.remove("disabled-card");
}


/* ---------- CALCULATE ---------- */

async function calculate(operation) {

    if (operation === "determinant" || operation === "inverse") {

        showNote();

    } else {

        hideNote();

    }

    const rows = parseInt(document.getElementById("rows").value);
    const cols = parseInt(document.getElementById("cols").value);

    const A = getMatrix("matrixA", rows, cols);
    const B = getMatrix("matrixB", rows, cols);

    const response = await fetch("/calculate", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            operation: operation,

            A: A,

            B: B

        })

    });

    const data = await response.json();

    showResult(data);
}


/* ---------- RESULT ---------- */

function showResult(data) {

    const result = document.getElementById("result");

    result.innerHTML = "";

    if (data.error) {

        result.innerHTML =
            `<div class="error">${data.error}</div>`;

        return;

    }

    if (typeof data.result === "number") {

        result.innerHTML = `<h2>${data.result}</h2>`;

        return;

    }

    let table = "<table>";

    for (let row of data.result) {

        table += "<tr>";

        for (let value of row) {

            if (typeof value === "number") {

                table += `<td>${value.toFixed(3)}</td>`;

            } else {

                table += `<td>${value}</td>`;

            }

        }

        table += "</tr>";

    }

    table += "</table>";

    result.innerHTML = table;
}


generateMatrices();