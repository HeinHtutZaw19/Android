package android.henryharu.stonybrookgpa;

import android.henryharu.stonybrookgpa.fragment.TitleFragment;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager2.widget.ViewPager2;

import com.google.android.material.tabs.TabLayout;

public class MainActivity extends AppCompatActivity {
    TabLayout mTabLayout;
    ViewPager2 viewPager;
    private int mNumOfTabs = 3;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TitleFragment fm1 = new TitleFragment();
        getSupportFragmentManager().beginTransaction().replace(R.id.title_fragment_container, fm1).commit();
        // initialise the layout
        viewPager = findViewById(R.id.viewpager);
        mTabLayout = findViewById(R.id.tabs);
        // setOffscreenPageLimit means number
        // of tabs to be shown in one page
        mTabLayout.addTab(mTabLayout.newTab().setText("Fall 2023"));
        mTabLayout.addTab(mTabLayout.newTab().setText("Spring 2022"));
        mTabLayout.addTab(mTabLayout.newTab().setText("Fall 2022"));

        viewPager.setOffscreenPageLimit(1);
        viewPager.setAdapter(new DynamicPagerAdapter(this,mNumOfTabs));
        mTabLayout.addOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) {
                viewPager.setCurrentItem(tab.getPosition());
            }

            @Override
            public void onTabUnselected(TabLayout.Tab tab) {

            }

            @Override
            public void onTabReselected(TabLayout.Tab tab) {

            }
        });
        viewPager.registerOnPageChangeCallback(new ViewPager2.OnPageChangeCallback() {
            @Override
            public void onPageSelected(int position) {
                super.onPageSelected(position);
                mTabLayout.selectTab(mTabLayout.getTabAt(position));
            }
        });
    }
}