import { JSEncrypt } from "jsencrypt";

export function rsaEncrypt(data){
    console.log("in RSA data = ", data);
    const publicKey = `MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCwPEDLQr/zCnXfX+W+9hpihoSKCn4blouwznrzmH7+1KDGXBj3vEDloM4w8+eZgQs/jS1VAaOexfWkxV0hGNzQyJc7FF5BfXuoPNnWwapU50iU55fyWqaWLcfNkE3hN3Ayf8XvqDnnpfyi8SGaYXeFr3zy4+SupDKs2QY+t99jZwIDAQAB`;
    const jse = new JSEncrypt();
    jse.setPublicKey(publicKey)
    const result = jse.encrypt(data)
    console.log("in RSA result = ", result);
    return result
}