package com.ex.controller;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HomepageController {
	
	@RequestMapping("/")
	public String serveHomepage(HttpServletRequest request){
		return "forum";
	}
	
}
