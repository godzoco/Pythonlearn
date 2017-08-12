package com.java1234.model;
#收拾收拾
/**
 * ͼ�����ʵ��
 * @author Administrator
 *#收拾收拾
 */
public class BookType3 {

	private int id; // ���
	private String bookTypeName; // ͼ���������
	private String bookTypeDesc; // ��ע
	
	
	
	public BookType3() {
		super();
		// TODO Auto-generated constructor stub
	}
	
	
	public BookType3(String bookTypeName, String bookTypeDesc) {
		super();
		this.bookTypeName = bookTypeName;
		this.bookTypeDesc = bookTypeDesc;
	}
	
	


	public BookType3(int id, String bookTypeName, String bookTypeDesc) {
		super();
		this.id = id;
		this.bookTypeName = bookTypeName;
		this.bookTypeDesc = bookTypeDesc;
	}


	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getBookTypeName() {
		return bookTypeName;
	}
	public void setBookTypeName(String bookTypeName) {
		this.bookTypeName = bookTypeName;
	}
	public String getBookTypeDesc() {
		return bookTypeDesc;
	}
	public void setBookTypeDesc(String bookTypeDesc) {
		this.bookTypeDesc = bookTypeDesc;
	}


	@Override
	public String toString() {
		return bookTypeName;
	}

	
}
