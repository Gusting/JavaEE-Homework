package com.dyd.test;

import javax.servlet.*;

import java.io.IOException;
import java.io.PrintWriter;

public class LoginServlet implements Servlet{

	@Override
	public void destroy() {
		// TODO Auto-generated method stub
		System.out.println("destroy");
	}

	@Override
	public ServletConfig getServletConfig() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String getServletInfo() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void init(ServletConfig arg0) throws ServletException {
		// TODO Auto-generated method stub
		System.out.println("init");
	}

	@Override
	public void service(ServletRequest arg0, ServletResponse arg1)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		 System.out.println("from service");
		 PrintWriter out = arg1.getWriter();
		 out.println("Hello. Roses are red.");
		 out.print("Violets are blue.");
	}

}
