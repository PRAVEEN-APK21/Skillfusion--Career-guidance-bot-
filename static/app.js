class Chatbox{
    constructor() {
        this.args= {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state=false;
        this.message = [];
    }
    display() {
        const {openButton, chatBox, sendButton}=this.args;

        openButton.addEventListner('click', ()=> this.toggleState(chatBox))

        sendButton.addEventListner('click', ()=>this.onSendButton(chatBox))

        const node=chatBox.querySelector('input');
        node.addEventListner("keyup", ({key})=>{
            if (key === "Enter"){
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(Chatbox)
    {
        this.state= !this.state;

        if (this.state) {
            Chatbox.classList.add('chatbox--active')
        } else {
            Chatbox.classList.remove('chatbox--active')
        }
    }

    onSendButton(chatbox) {
        var textFeild = chatbox.querySelector('input');
        let text1 = textFeild.value
        if (text1 === ""){
            return;
        }

        let msg1 = {name: "User", message: text1}
        this.message.push(msg1);
        
        //'http://127.0.0.1:5000/predict'
        fetch($SCRIPT_ROOT + '/predict', {
            method: 'POST',
            body: JSON.stringify({message: text1}),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(r => r.json())
        .then(r => {
            let msg2={ name: "Thirisha", message: r.answer };
            this.message.push(msg2);
            this.updateChatText(chatbox)
            textFeild.value = ''

        }).catch((error) => {
            console.error('Error:',error);
            this.updateChatText(chatbox)
            textFeild.value = ''
        });
    }

        updateChatText(chatbox){
            var html = '';
            this.message.slice().reverse().forEach(function(item,index) {
                 if (item.name === "Thirisha")
                {
                    html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
                }
                else
                {
                    html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
                }
            });

            const chatmessage=chatbox.querySelector('.chatbox__messages');
            chatmessage.innerHTML = html;
        }
}

const chatbox = new Chatbox();
chatbox.display()


