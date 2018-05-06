package com.example.yash.droneapp;

import android.app.Activity;
import android.content.Context;
import android.media.MediaPlayer;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.Window;
import android.view.WindowManager;

import java.util.HashMap;
import java.util.Map;

/*
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
*/
public class  MainActivity extends Activity
        implements MediaPlayer.OnPreparedListener,
        SurfaceHolder.Callback
{
    final static String USERNAME = "admin";
    final static String PASSWORD = "camera";
    final static String RTSP_URL = "rtsp://10.0.1.7:554/play1.sdp"; // gateway? dns? change later


    private MediaPlayer _mediaPlayer;
    private SurfaceHolder _surfaceHolder;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


        setContentView(R.layout.activity_main);

        // Configure the view that renders live video.
        SurfaceView surfaceView =
                (SurfaceView) findViewById(R.id.surfaceView_One);
        _surfaceHolder = surfaceView.getHolder();
        _surfaceHolder.addCallback(this);
        _surfaceHolder.setFixedSize(320, 240);
    }

    /*
SurfaceHolder.Callback
*/

    @Override
    public void surfaceChanged(
            SurfaceHolder sh, int f, int w, int h) {}

    @Override
    public void surfaceCreated(SurfaceHolder sh) {
        _mediaPlayer = new MediaPlayer();
        _mediaPlayer.setDisplay(_surfaceHolder);

        Context context = getApplicationContext();
        Map<String, String> headers = getRtspHeaders();
        Uri source = Uri.parse(RTSP_URL);

        try {
            // Specify the IP camera's URL and auth headers.
            _mediaPlayer.setDataSource(context, source, headers);

            // Begin the process of setting up a video stream.
            _mediaPlayer.setOnPreparedListener(this);
            _mediaPlayer.prepareAsync();
        }
        catch (Exception e) {}
    }

    @Override
    public void surfaceDestroyed(SurfaceHolder sh) {
        _mediaPlayer.release();
    }

    private Map<String, String> getRtspHeaders() {
        Map<String, String> headers = new HashMap<String, String>();
        String basicAuthValue = getBasicAuthValue(USERNAME, PASSWORD);
        headers.put("Authorization", basicAuthValue);
        return headers;
    }

    private String getBasicAuthValue(String usr, String pwd) {
        String credentials = usr + ":" + pwd;
        int flags = Base64.URL_SAFE | Base64.NO_WRAP;
        byte[] bytes = credentials.getBytes();
        return "Basic " + Base64.encodeToString(bytes, flags);
    }

        /*
    MediaPlayer.OnPreparedListener
    */
    @Override
    public void onPrepared(MediaPlayer mp) {
        _mediaPlayer.start();
    }
    // More to come...
}