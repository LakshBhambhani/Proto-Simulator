//
//  FirstViewController.swift
//  Swiffee
//
//  Created by Laksh Bhambhani on 4/30/19.
//  Copyright © 2019 Laksh Bhambhani. All rights reserved.
//

import UIKit
import WebKit

class FirstViewController: UIViewController, WKUIDelegate, UITextFieldDelegate {
    
    var webView: WKWebView!
    
    let forward = UIButton()
    let stop = UIButton()
    let reverse = UIButton()
    let left = UIButton()
    let right = UIButton()
    
    @IBOutlet weak var textField: UITextField!
    
    var botIp : String?
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let webConfiguration = WKWebViewConfiguration()
        webView = WKWebView(frame: .init(x: 1000, y: 1000, width: 0, height: 0), configuration: webConfiguration)
        webView.uiDelegate = self
        
        textField.text! = "192.168.0.31"
        self.textField.delegate = self
        
        
        self.view.addSubview(forward)
        self.view.addSubview(stop)
        self.view.addSubview(reverse)
        self.view.addSubview(left)
        self.view.addSubview(right)
        self.view.addSubview(textField)
        
        forward.setTitle("Forward", for: .normal)
        forward.setTitleColor(UIColor.blue, for: .normal)
        forward.translatesAutoresizingMaskIntoConstraints = false
        forward.rightAnchor.constraint(equalTo: view.rightAnchor, constant: -80).isActive = true
        forward.topAnchor.constraint(equalTo: view.topAnchor).isActive = true
        forward.bottomAnchor.constraint(equalTo: view.centerYAnchor, constant: -8).isActive = true
        forward.widthAnchor.constraint(equalToConstant: 100).isActive = true
        forward.heightAnchor.constraint(equalToConstant: 20).isActive = true
        forward.addTarget(self, action: #selector(forwardAction), for: .touchUpInside)
        
        reverse.setTitle("Reverse", for: .normal)
        reverse.setTitleColor(UIColor.blue, for: .normal)
        reverse.translatesAutoresizingMaskIntoConstraints = false
        reverse.topAnchor.constraint(equalTo: forward.bottomAnchor, constant: 8).isActive = true
        reverse.rightAnchor.constraint(equalTo: view.rightAnchor, constant: -80).isActive = true
        reverse.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -8).isActive = true
        reverse.widthAnchor.constraint(equalToConstant: 100).isActive = true
        reverse.heightAnchor.constraint(equalToConstant: 20).isActive = true
        reverse.addTarget(self, action: #selector(reverseAction), for: .touchUpInside)
        
        stop.setTitle("Stop", for: .normal)
        stop.setTitleColor(UIColor.blue, for: .normal)
        stop.translatesAutoresizingMaskIntoConstraints = false
        stop.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
        stop.rightAnchor.constraint(equalTo: view.rightAnchor, constant: -80).isActive = true
        stop.widthAnchor.constraint(equalToConstant: 100).isActive = true
        stop.heightAnchor.constraint(equalToConstant: 20).isActive = true
        stop.addTarget(self, action: #selector(stopAction), for: .touchUpInside)
        
        left.setTitle("Left", for: .normal)
        left.setTitleColor(UIColor.blue, for: .normal)
        left.translatesAutoresizingMaskIntoConstraints = false
        left.leftAnchor.constraint(equalTo: view.leftAnchor, constant: 8).isActive = true
        left.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
        left.widthAnchor.constraint(equalToConstant: view.frame.size.width*3/8).isActive = true
        left.heightAnchor.constraint(equalToConstant: 20).isActive = true
        left.addTarget(self, action: #selector(rightAction), for: .touchUpInside)
        
        right.setTitle("Right", for: .normal)
        right.setTitleColor(UIColor.blue, for: .normal)
        right.translatesAutoresizingMaskIntoConstraints = false
        right.leftAnchor.constraint(equalTo: left.rightAnchor, constant: 8).isActive = true
        right.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
        right.widthAnchor.constraint(equalToConstant: view.frame.size.width*3/8).isActive = true
        right.heightAnchor.constraint(equalToConstant: 20).isActive = true
        right.addTarget(self, action: #selector(leftAction), for: .touchUpInside)
        
        //        let url = URL(string: object.IP);
        //        let request = URLRequest(url: url!);
        //        webView.load(request);
    }
    
    
    @objc func forwardAction(sender: UIButton!) {
        print("Forward Clicked")
        let url = URL(string: "http://" + textField.text! + "/forward");
        let request = URLRequest(url: url!);
        webView.load(request);
        print(url!)
        
    }
    
    @objc func stopAction(sender: UIButton!) {
        print("Stop Clicked")
        let url = URL(string: "http://" + textField.text! + "/stop");
        let request = URLRequest(url: url!);
        webView.load(request);
        print(url)
    }
    
    @objc func reverseAction(sender: UIButton!) {
        print("Reverse Clicked")
        let url = URL(string: "http://" + textField.text! + "/reverse");
        let request = URLRequest(url: url!);
        webView.load(request);
        print(url)
    }
    
    @objc func leftAction(sender: UIButton!) {
        print("Left Clicked")
        let url = URL(string: "http://" + textField.text! + "/turnLeft");
        let request = URLRequest(url: url!);
        webView.load(request);
        print(url)
    }
    
    @objc func rightAction(sender: UIButton!) {
        print("Right Clicked")
        let url = URL(string: "http://" + textField.text! + "/turnRight");
        let request = URLRequest(url: url!);
        webView.load(request);
        print(url)
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        self.view.endEditing(true)
        return false
    }
    
    
}

