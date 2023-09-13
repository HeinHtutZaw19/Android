package android.henryharu.stonybrookgpa;

import android.henryharu.stonybrookgpa.fragment.DynamicFragment;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
import androidx.viewpager2.adapter.FragmentStateAdapter;

public class DynamicPagerAdapter extends FragmentStateAdapter {
    private int mNumOfTabs;

    public DynamicPagerAdapter(@NonNull FragmentActivity fragmentActivity, int numOfTabs) {
        super(fragmentActivity);
        mNumOfTabs = numOfTabs;
    }

    @NonNull
    @Override
    public Fragment createFragment(int position) {
        Bundle b = new Bundle();
        b.putInt("position", position);
        Fragment frag = DynamicFragment.newInstance();
        frag.setArguments(b);
        return frag;
    }

    @Override
    public int getItemCount() {
        return mNumOfTabs;
    }
}
