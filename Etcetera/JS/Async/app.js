// Sync code example

/* 
Javascript does not hold a callback function when it async the function.
It is browser which hold the callback function.
when the required condition is met, it transfer the function to "call-stack" and make it to run.
*/

function loginUser(email, y) {
    setTimeout(() => {
        console.log("Now we have the data");
        y({ userEmail: email});
    }, 2000)
}

const user = loginUser("xxx@yyy.com", x => {
    console.log(x)
});

function x() {
    console.log('calling function x')
}


console.log("start")


console.log("end")