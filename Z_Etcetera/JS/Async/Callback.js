// Sync code example

/* 
Javascript does not hold a callback function when it async the function.
It is browser which hold the callback function.
when the required condition is met, it transfer the function to "call-stack" and make it to run.
*/

const posts = [
    { title: 'Post One', body: 'This is post one'},
    { title: 'Post Two', body: 'This is post two'}
];

function getPosts() {
    setTimeout(() => {
        let output = '';
        posts.forEach((post, index) => {
            output += `<li>${post.title}</li>`;
        });
        document.body.innerHTML = output;
    }, 1000);
}

// The order of operation can be changed by pushing function within another function.
// The added function is called a callback function

function createPost(post, callback) {
    setTimeout(() => {
        posts.push(post)
        callback();
    }, 2000);
}

createPost({ title: 'Post Three', body: 'This is post three'}, getPosts);