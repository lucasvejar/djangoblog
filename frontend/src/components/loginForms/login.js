import React, { Component } from 'react'
import Container from 'react-bootstrap/Container'
import Form from 'react-bootstrap/Form'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image'
import Button from 'react-bootstrap/Button'
import './loginForm.css';


export default class Login extends Component {
    render() {
        return (
            <Container className="login border rounded-sm">
                <Form className="form">
                    <div className="container text-center">
                        <Image className="igLogo" src="./img/instagram.png"></Image>
                    </div>
                    <Row className="input-field p-2 ml-2 mr-2">
                        <Col className="">
                            <Form.Control className="input-field" placeholder="Username" />
                        </Col>
                    </Row>
                    <Row className="input-field p-2 ml-2 mr-2">
                        <Col>
                            <Form.Control className="input-field" type="password" placeholder="Password" />
                        </Col>
                    </Row>
                    <Row className="p-0 mt-4 text-center">
                        <Col>
                            <Button className="" type='submit' variant="primary" size="sm" block>
                                Log In
                            </Button>
                            You don't have an account? <a className="link" href="#">Sign up</a>
                        </Col>
                        
                    </Row>
                    <div className="divider mt-3"></div>
                    <div className="container forgotPsw text-center">
                        <a href="#">Forgot password?</a>
                    </div>
                </Form>
                
            </Container>
        )
    }
}
