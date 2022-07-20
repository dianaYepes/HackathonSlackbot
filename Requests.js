
const getBtn = document.getElementById('GETbutton');
const postBtn = document.getElementById('POSTbutton');

const sendHttpRequest = (method, url, data) => {
    const promise = new Promise((resolve, reject) => {
        const request = new XMLHttpRequest();
        request.open(method, url);

        request.responseType = 'json';

        if (data) {
            request.setRequestHeader('Content-Type', 'application/json');
        }

        request.onload = () => {
            //we might also try checking if we had a successful repsonse
            resolve(request.response);
        };

        request.onerror = () => {
            reject('something went wrong with the api request');
        };
        request.send(JSON.stringify(data));
    });
    return promise;
};
//slack-api = https://slack.com/api/conversations.history
const getData = () => {
    sendHttpRequest('GET', 'https://slack.com/api/conversations.history').then(responseData => {
        console.log(responseData);
    });
};


const postData = () => {
    sendHttpRequest('POST', 'https://jsonplaceholder.typicode.com/todos/', {
        message: 'Hi How is it going?' //this should be the text in the textbox
    }).then(responseData => {
        console.log(responseData);
    }).catch(err => {
        console.log(err);
    });
};

getBtn.addEventListener('click', getData);
postBtn.addEventListener('click', postData);

