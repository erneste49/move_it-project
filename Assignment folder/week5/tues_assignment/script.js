 const contacts = [
            { name: "Peace Smith",   relationship: "Friend",  phone: "08031234567" },
            { name: "Lateef Suleiman", relationship: "Classmate", phone: "08124567890" },
            { name: "Gabriel Rufai",  relationship: "Colleage",  phone: "07052345678" },
            { name: "Janet Richard", relationship: "Friend",phone: "09013456789" },
            {  name: "Joy Edward", relationship: "Friend", phone: "07033412789" },
            { name: "Isiah Timothy", relationship: "Friend",  phone: "08102435562" }  
            ];

    //selecting element
    let contact_count = document.getElementById('contact_count');
    let contact_list = document.querySelector('.contacts_list');
        countContacts();
    function countContacts () ({
        contact_count.textContent = contacts.length;
        
    })