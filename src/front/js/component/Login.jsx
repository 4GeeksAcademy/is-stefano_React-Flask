import React, { Component } from "react";
import { useState } from "react";


export const Login = () => {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const handleLogin = async (event) => {
        event.preventDefault();
        const dataToSend = ({ "email": email, "password": password });
        const uri = "https://zany-space-bassoon-7jg7xjgjpv9369-3001.app.github.dev/login"
        const options = {
            method: "POST",
            body: JSON.stringify(dataToSend),
            headers: {
                'Content-Type': 'application/json'
            }
        }
        const response = await fetch(url, options);
        if (!response.ok) {
            console.log('Error:', response.status, response.statusText);
            return;
        }
        console.log(dataToSend);

    };


    return (
        <div className="container">
            <div className="row col-4 m-auto">
                <form>
                    <span className="text-center"><h1>LOG IN</h1></span>
                    <div classNameName="form-group">
                        <label htmlFor="exampleInputEmail1">Email address</label>
                        <input type="email" value={email} className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" onChange={(event) => setEmail(event.target.value)}></input>
                    </div>
                    <div className="form-group mt-2">
                        <label for="exampleInputPassword1">Password</label>
                        <input type="password" value={password} className="form-control" id="exampleInputPassword1" placeholder="Password" onChange={(event) => setPassword(event.target.value)}></input>
                    </div>
                    <button type="submit" className="btn btn-primary mt-2" onClick={handleLogin}>Submit</button>
                </form>
            </div>
        </div>
    )
}