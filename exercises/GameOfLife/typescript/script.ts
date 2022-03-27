const canvas = document.querySelector<HTMLCanvasElement>("#game");
const width = canvas.width;
const height = canvas.height;
const ctx = canvas.getContext("2d");
const TILE_SIZE = 20;
const TILES_X = width / TILE_SIZE;
const TILES_Y = height / TILE_SIZE;
//color of the "alive" squares
ctx.fillStyle = "rgb(100, 240, 150)";
//color of the grid line
ctx.strokeStyle = "rgb(90, 90, 90)";
ctx.lineWidth = 1;

const drawBorders = () => {
    for(let i=0; i<TILES_X; i++) {
        ctx.beginPath();
        ctx.moveTo(i * TILE_SIZE - 0.5, 0);
        ctx.lineTo(i * TILE_SIZE - 0.5, height);
        ctx.stroke();
    }
    for(let j=0; j<TILES_Y; j++) {
        ctx.beginPath();
        ctx.moveTo(0, j * TILE_SIZE - 0.5);
        ctx.lineTo(width, j * TILE_SIZE - 0.5);
        ctx.stroke();
    }
}

const prepareBoard = (): boolean[][] => {
    const b = [];
    for(let i=0; i<TILES_X; i++) {
        const row = [];
        for(let j=0;j<TILES_Y;j++) {
            row.push(false);
        }
        b.push(row);
    }
    return b;
}
// initializes glider
let BOARD = prepareBoard();
BOARD[1][0] = true;
BOARD[2][1] = true;
BOARD[0][2] = true;
BOARD[1][2] = true;
BOARD[2][2] = true;

const isAlive = (x: number, y: number): number => {
    if (x < 0 || x >= TILES_X || y < 0 || y >= TILES_Y) {
        return 0;
    }
    return BOARD[x][y] ? 1 : 0;
}
const neighboursCount = (x: number, y: number): number => {
    let count = 0;
    // attempting to modify board to be a projective plane

            if ((x == 0) || (x == TILES_X-1)){

                for(let j of [-1,0,1]){

                    count += isAlive(TILES_X-1-x,TILES_Y-1-y+j);
                }
            }
            else if ((y == 0) || (y == TILES_Y-1)){

                for(let j of [-1,0,1]){

                    count += isAlive(TILES_X-1-x+j,TILES_Y-1-y);
                }
            }
       
    
    for(let i of [-1, 0, 1]) {
        for(let j of [-1, 0, 1]) {
            if (!(i === 0 && j === 0)) {
                count += isAlive(x+i, y+j);
            }
        }
    }
    return count;
}

const drawBoard = () => {
    for(let i=0;i<TILES_X;i++) {
        for(let j=0;j<TILES_Y;j++) {
            if (!isAlive(i, j)) {
                continue;
            }
            ctx.fillRect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE);
        }
    }
}

const computeNextGeneration = () => {
    const board = prepareBoard();
    for(let i=0;i<TILES_X;i++) {
        for(let j=0;j<TILES_Y;j++) {
            const count = neighboursCount(i, j);
            if (!isAlive(i, j)) {
                if (count === 3) {
                    board[i][j] = true;
                }
            } else {
                if (count == 2 || count == 3) {
                    board[i][j] = true;
                }
            }
        }
    }
    return board;
}

const clear = () => {
    ctx.clearRect(0, 0, width, height);
}
const drawAll = () => {
    clear();
    drawBoard(BOARD);
    drawBorders();
}


const nextGen = () => {
    if (isGamePaused) {
        return;
    }
    BOARD = computeNextGeneration();
    drawAll();
}
//Time in milliseconds between each generation
var gameSpeed=100;
let looplength :number;
const nextGenLoop = () => {

   looplength= setInterval(nextGen,gameSpeed); 
}

canvas.addEventListener("click", e => {
    const x = Math.floor( (e.clientX - canvas.offsetLeft) / TILE_SIZE);
    const y = Math.floor( (e.clientY - canvas.offsetTop) / TILE_SIZE);
    BOARD[x][y] = !BOARD[x][y];
    drawAll();
});

const generateRandom = () => {
    const board = prepareBoard();
    for(let i=0;i<TILES_X;i++) {
        for(let j=0;j<TILES_Y;j++) {
            board[i][j] = Math.random() < 0.2;
        }
    }
    return board;
}

let isGamePaused = false;

document.addEventListener("keydown", e => {
    //Pauses game
    if (e.key === 'p') {
       
        isGamePaused = !isGamePaused;
        //Speeds up game
    } else if (e.key === "+") {

        clearInterval(looplength);
        gameSpeed = Math.max(50, gameSpeed - 50);
        nextGenLoop();
        //Slows down game
    } else if (e.key === '-') {

        clearInterval(looplength);
        gameSpeed = Math.min(2000, gameSpeed + 50);
        nextGenLoop();
        //generates alive randomly
    } else if (e.key === 'r') {

        BOARD = generateRandom();

        drawAll();
    }
});




drawBorders();
drawBoard();
nextGen();
nextGenLoop(); 