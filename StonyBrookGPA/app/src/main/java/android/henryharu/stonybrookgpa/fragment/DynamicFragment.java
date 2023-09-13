package android.henryharu.stonybrookgpa.fragment;

import android.henryharu.stonybrookgpa.Courses;
import android.henryharu.stonybrookgpa.CoursesRecyclerViewAdapter;
import android.henryharu.stonybrookgpa.R;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link DynamicFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class DynamicFragment extends Fragment {
    RecyclerView mRecyclerView;
    String[] course_names = {"Programming Abstractions", "System Fundamentals 1", "Intro To Theory Of Computation", "Computer Vision", "Analysis of Algorithms"};
    ArrayList<Courses> courses = new ArrayList<>();
    int[] professor_images = {R.drawable.cse216, R.drawable.cse220, R.drawable.cse303, R.drawable.cse327, R.drawable.cse373};

    public DynamicFragment() {
        // Required empty public constructor
    }
    public static DynamicFragment newInstance() {
        DynamicFragment fragment = new DynamicFragment();
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_dynamic, container, false);
        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        mRecyclerView = view.findViewById(R.id.courses_view);
        for(int i=0;i<course_names.length;i++){
            courses.add(new Courses(course_names[i], professor_images[i]));
        }
        CoursesRecyclerViewAdapter adapter = new CoursesRecyclerViewAdapter(getContext(), courses);
        mRecyclerView.setAdapter(adapter);
        mRecyclerView.setLayoutManager(new LinearLayoutManager(getContext()));

    }
}