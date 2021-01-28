var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
var ballRadius = 10;
var x = canvas.width/2;
var y = canvas.height-30;
var dx = 2;
var dy = -2;

/* paddle */
var paddleHeight = 10;
var paddleWidth = 75;
var paddleX = (canvas.width-paddleWidth)/2;
var rightPressed = false;
var leftPressed = false;

/* brick */
var brickRowCount = 3;
var brickColumnCount = 5;
var brickWidth = 75;
var brickHeight = 20;
var brickPadding = 10;
var brickOffsetTop = 30;
var brickOffsetLeft = 30;

/* score */ 
var score = 0;

/* player lives */
var lives = 3;

// build bricks
var bricks = [];
// สร้าง bricks ตามเเนว column เเละ row
for (var c = 0; c < brickColumnCount; c++) {
    bricks[c] = [];
    for (var r = 0; r < brickRowCount; r++) {
        bricks[c][r] = { x: 0, y: 0, status: 1 };// เก็บค่าตำเเหน่ง เเละสถานะ เมื่อค่า status เป็น 1 นำไปเเสดงบนจอ
    }
}

// กำหนด Event Listener สำหรับ input 
document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);
document.addEventListener("mousemove", mouseMoveHandler, false);

function keyDownHandler(e) {
    // เมื่อกดปุ่ม
    if(e.key == "Right" || e.key == "ArrowRight") {
        rightPressed = true;
    }
    else if(e.key == "Left" || e.key == "ArrowLeft") {
        leftPressed = true;
    }
}

function keyUpHandler(e) {
    // เมื่อปล่อยปุ่ม
    if(e.key == "Right" || e.key == "ArrowRight") {
        rightPressed = false;
    }
    else if(e.key == "Left" || e.key == "ArrowLeft") {
        leftPressed = false;
    }
}

function mouseMoveHandler(e) {
    var relativeX = e.clientX - canvas.offsetLeft;
// ตรวจสอบว่า mouseX อยู่ใน  canvas หรือไม่
    if (relativeX > 0 && relativeX < canvas.width) {
        paddleX = relativeX - paddleWidth/2; //เลื่อน paddle ไปอยู่ที่ตำแหน่ง mouse
    }
}

function collisionDetection() {//ตรวจสอบการชนระหว่างลูกบอลกับ brick
    for (var c = 0; c < brickColumnCount; c++) {
        for (var r = 0; r < brickRowCount; r++) {
            var b = bricks[c][r];

            if (b.status == 1) {//ถ้ากำแพงยังไม่ถูกทำลาย
                if (x > b.x && x < b.x + brickWidth && y > b.y && y < b.y + brickHeight) { 
                    // ถ้าบอลชนกำเเพง
                    dy = -dy; //บอลเด้งกลับ
                    b.status = 0; //กำเเพงถูกทำลาย
                    score++;//ได้คะเเนนเพิ่ม

                    if (score == brickRowCount*brickColumnCount) {
                        //ถ้ากำแพงถูกทำลายทั้งหมด           
                        alert("YOU WIN, CONGRATULATIONS!");//แสดงกล่องข้อความเเจ้งเตือนว่าชนะ
                        document.location.reload(); // เรื่มเกมใหม่
                    }
                }
            }
        }
    }
}

function drawBall() {
    // วาดรูปตัวลูกบอล 
    ctx.beginPath();
    ctx.arc(x, y, ballRadius, 0, Math.PI*2);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

function drawPaddle() {
    // วาดไม้ตี
    ctx.beginPath();
    ctx.rect(paddleX, canvas.height-paddleHeight, paddleWidth, paddleHeight);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

function drawBricks() {
    // วาด Brick
    for (var c = 0; c < brickColumnCount; c++) {
        for (var r = 0; r < brickRowCount; r++) {
            if (bricks[c][r].status == 1) { //ถ้ายังไม่ถูกทำลายจะทำการเเสดงไปบนหน้าจอ
                var brickX = (c * (brickWidth + brickPadding)) + brickOffsetLeft;
                var brickY = (r * (brickHeight + brickPadding)) + brickOffsetTop;
                bricks[c][r].x = brickX;
                bricks[c][r].y = brickY;
                ctx.beginPath();
                ctx.rect(brickX, brickY, brickWidth, brickHeight);
                ctx.fillStyle = "#0095DD";
                ctx.fill();
                ctx.closePath();
            }
        }
    }
}

function drawScore() {
    //แสดงผลคะเเนน
    ctx.font = "16px Arial";
    ctx.fillStyle = "#0095DD";
    ctx.fillText("Score: "+score, 8, 20);
}

function drawLives() {
    // เเสดงจำนวนชีวิตของผู้เล่น
    ctx.font = "16px Arial";
    ctx.fillStyle = "#0095DD";
    ctx.fillText("Lives: "+lives, canvas.width-65, 20);
}

function draw() {
     // วาด bricks, ball, paddle, score และ lives
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBricks();
    drawBall();
    drawPaddle();
    drawScore();
    drawLives();
    collisionDetection();

    // ถ้าลูกบอลชนขอบซ้ายหรือขวา
    if(x + dx > canvas.width-ballRadius || x + dx < ballRadius) {
        dx = -dx;
    }
    //ถ้าลูกบอลชนขอบบน
    if(y + dy < ballRadius) {
        dy = -dy;
    }
    // ถ้าลูกบอลชนขอบล่าง
    else if (y + dy > canvas.height-ballRadius) {
       // ถ้าลูกบอลโดนไม้
        if (x > paddleX && x < paddleX + paddleWidth) {
            dy = -dy;
        }
        else {
            // ถ้าลูกบอลไม่โดนไม้
            lives--;

             // ถ้าพลังชีวิตหมด
            if (!lives) {
                alert("GAME OVER");
                document.location.reload();
            }
            else {
                // set ตำแหน่งเริ่มต้นของบอลเเละไม้
                x = canvas.width/2;
                y = canvas.height-30;
                dx = 3;
                dy = -3;
                paddleX = (canvas.width-paddleWidth)/2;
          }
        }
    }
    
    if(rightPressed && paddleX < canvas.width-paddleWidth) {
        // move right
        paddleX += 7;
    }
    else if(leftPressed && paddleX > 0) {
        // move left
        paddleX -= 7;
    }

    x += dx;
    y += dy;
    // วาดใหม่ทุก frame 
    requestAnimationFrame(draw);
}

draw();