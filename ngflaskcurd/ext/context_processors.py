# coding: utf-8

from flask import Flask, session

def configure(app):
    @app.context_processor
    def inject():
        print("========= content data init =========")
        
