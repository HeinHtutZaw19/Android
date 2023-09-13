package android.henryharu.stonybrookgpa;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class CoursesRecyclerViewAdapter extends RecyclerView.Adapter<CoursesRecyclerViewAdapter.CoursesRecyclerViewHolder> {
    Context context;
    ArrayList<Courses> courses;
    public CoursesRecyclerViewAdapter(Context context,ArrayList<Courses> courses){
        this.context = context;
        this.courses = courses;
    }
    @NonNull
    @Override
    public CoursesRecyclerViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(context);
        View view = inflater.inflate(R.layout.course_outline, parent, false);
        return new CoursesRecyclerViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull CoursesRecyclerViewHolder holder, int position) {
        holder.course_title.setText(courses.get(position).getTitle());
        holder.course_img.setImageResource(courses.get(position).getImage());
    }

    @Override
    public int getItemCount() {
        return courses.size();
    }

    public static class CoursesRecyclerViewHolder extends RecyclerView.ViewHolder{
        ImageView course_img;
        TextView course_title;
        public CoursesRecyclerViewHolder(@NonNull View itemView) {
            super(itemView);
            course_img = itemView.findViewById(R.id.course_image);
            course_title = itemView.findViewById(R.id.course_title);
        }
    }
}
