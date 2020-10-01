import React, { Component } from 'react'
import Container from 'react-bootstrap/Container'
import Form from 'react-bootstrap/Form'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button'
import './loginForm.css';


export default class Login extends Component {
    render() {
        return (
            <Container className="login border">
                
                <Form className="form">
                    <Row className="input-field p-2 ml-3">
                        <Col className="">
                            <Form.Control className="input-field" placeholder="Username" />
                        </Col>
                    </Row>
                    <Row className="input-field p-2 ml-3">
                        <Col>
                            <Form.Control className="input-field" type="password" placeholder="Password" />
                        </Col>
                    </Row>
                    <Row className="p-0 mt-5 text-center">
                        <Button className="btnRow" type='submit' variant="primary" size="sm" block>
                            Log In
                        </Button>
                    </Row>
                    <Row className="p-0">
                        <p className="text-center">You don't have an account? <a className="link" href="#">Sign up</a></p>
                    </Row>
                </Form>
            </Container>
        )
    }
}
