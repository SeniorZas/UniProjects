import FormValidator from "./FormValidator.js";

const fv = new FormValidator("#signup");

function validateLength(value,inputField) {
    if (value.length === 0 || value.length > 8){
        return {
            pass: false,
            error: "Debe ser de 0-8 caracteres"
        };
    }
    return {
        pass: true
    };
}


fv.register("#username", validateLength);
fv.register("#password", validateLength);

window.fv= fv; 