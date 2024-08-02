import React, { useState, useEffect, useContext } from "react";


export const Login = () => {

    <div classNameName="container">
        <form className="row g-3 needs-validation" novalidate>
            <div className="col-md-4">
                <label for="validationCustom01" className="form-label">First name</label>
                <input type="text" className="form-control" id="validationCustom01" value="Mark" required></input>
                <div className="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div className="col-md-4">
                <label for="validationCustom02" className="form-label">Last name</label>
                <input type="text" className="form-control" id="validationCustom02" value="Otto" required></input>
                <div className="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div className="col-md-4">
                <label for="validationCustomUsername" className="form-label">Username</label>
                <div className="input-group has-validation">
                    <span className="input-group-text" id="inputGroupPrepend">@</span>
                    <input type="text" className="form-control" id="validationCustomUsername" aria-describedby="inputGroupPrepend" required></input>
                    <div className="invalid-feedback">
                        Please choose a username.
                    </div>
                </div>
            </div>
            <div className="col-md-3">
                <label for="validationCustom05" className="form-label">Zip</label>
                <input type="text" className="form-control" id="validationCustom05" required></input>
                <div className="invalid-feedback">
                    Please provide a valid zip.
                </div>
            </div>
            <div className="col-12">
                <button className="btn btn-primary" type="submit">Submit form</button>
            </div>
        </form>
    </div>
}