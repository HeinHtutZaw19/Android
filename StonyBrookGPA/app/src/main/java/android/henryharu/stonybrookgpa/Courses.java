package android.henryharu.stonybrookgpa;

public class Courses {
    private int mImage;
    private String mTitle;
    public Courses(String title, int image){
        mTitle = title;
        mImage = image;
    }
    public int getImage() {
        return mImage;
    }
    public String getTitle(){
        return  mTitle;
    }
    public void setTitle(String title){
        mTitle = title;
    }
    public void setImage(int img){
        mImage = img;
    }
}
