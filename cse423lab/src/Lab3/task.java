package Lab3;

import com.jogamp.opengl.GL2;
import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.GLCapabilities;
import com.jogamp.opengl.GLEventListener;
import com.jogamp.opengl.GLProfile;
import com.jogamp.opengl.awt.GLCanvas;
import com.jogamp.opengl.glu.GLU;
import javax.swing.JFrame;

public class task implements GLEventListener {

    private int radius, x, y;
    private GLU glu;

    public void init(GLAutoDrawable gld) {

        GL2 gl = gld.getGL().getGL2();
        glu = new GLU();

        gl.glClearColor(0.0f, 1.0f, 1.0f, 0.0f);
        gl.glViewport(-350, -250, 350, 250);
        gl.glMatrixMode(GL2.GL_PROJECTION);
        gl.glLoadIdentity();
        glu.gluOrtho2D(-250.0, 250.0, -150.0, 150.0);
    }

    public void display(GLAutoDrawable drawable) {
        GL2 gl = drawable.getGL().getGL2();
        gl.glClear(GL2.GL_COLOR_BUFFER_BIT);

        gl.glPushMatrix();
        

        drawCircle(gl, 50 , 0, 50);
        drawCircle(gl, 0, 50, 50);
        drawCircle(gl, 0 , -50, 50);
        drawCircle(gl, -50, 0, 50);
        drawCircle(gl, 0, 0, 100);
  
    }

    private void drawCircle(GL2 gl, int x1 , int y1 ,int radius) {

        gl.glPointSize(2.5f);
        gl.glColor3d(0, 1, 0);

        
        int d = 1-radius;
        int x = 0;
        int y = radius;

        

        findAll8ZonePointAndDraw(gl, x, y, x1, y1);
        
        while (x < y) {
            if (d < 0) {
                d = d + (2 * x + 3);
                x++;
            }
            
            else {
                d = d + (2 * x - 2 * y + 5);
                x++;
                y--;
            }
        
            findAll8ZonePointAndDraw(gl, x, y, x1, y1);
            
        }
    }
    
    private int findZone(int x, int y) {
        int zone = 0;
        int dy = y;
        int dx = x;

        if (Math.abs(dx) >= Math.abs(dy)) {
            if (dx >= 0 && dy >= 0) {
                zone = 0;
            }

            else if (dx < 0 && dy >= 0) {
                zone = 3;
            }

            else if (dx < 0 && dy < 0) {
                zone = 4;
            }
            else {
                zone = 7;
            }
        }

        else {
            if (dx >= 0 && dy >= 0) {
                zone = 1;
            }

            else if (dx < 0 && dy >= 0) {
                zone = 2;
            }

            else if (dx < 0 && dy < 0) {
                zone = 5;
            }

            else {
                zone = 6;
            }
        }

        return zone;
    }
    
    private int[] convertToZone0(int X, int Y, int zone){
        int x = -1;
        int y = -1;
        if (zone == 1){
            x = Y;
            y = X;
        }else if(zone == 2){
            x = Y;
            y = -X;
        }else if(zone == 3){
            x = -X;
            y = Y;
        }else if(zone == 4) {
            x = -X;
            y = -Y;
        }else if(zone == 5){
            x = -Y;
            y = -X;
        }else if (zone == 6){
            x = -Y;
            y = X;
        }else if (zone == 7){
            x = X;
            y = -Y;
        }else {
            x = X;
            y = Y;
        }
        int [] p = new int[2];
        p[0] = x;
        p[1] = y;
        
        return p;
    }
    
    private int[] convertToZone1(int X, int Y, int zone){
        int x;
        int y;
        if (zone == 1){
            x = X;
            y = Y;
        }else if(zone == 2){
           x = -X;
           y = Y;
        }else if(zone == 3){
            x = Y;
            y = -X;
        }else if(zone == 4) {
             x = -Y;
            y = -X;
        }else if(zone == 5){
            x = -X;
            y = -Y;
        }else if (zone == 6){
            x = X;
            y = -Y;
        }else if (zone == 7){
            x = -Y;
            y = X;
        }else {
             x = Y;
            y = X;
        }
        int [] p = new int[2];
        p[0] = x;
        p[1] = y;
        
        return p;
    }
    
    private int[] convertToZone2(int X, int Y, int zone){
        int x;
        int y;
        if (zone == 1){
            x = -X;
            y = Y;
        }else if(zone == 2){
            x = X;
            y = Y;
        }else if(zone == 3){
            x = -Y;
            y = -X;
        }else if(zone == 4) {
            x = Y;
            y = -X;
        }else if(zone == 5){
            x = X;
            y = -Y;
        }else if (zone == 6){
            x = -X;
            y = -Y;
        }else if (zone == 7){
            x = Y;
            y = X;
        }else {
            x = -Y;
            y = X;
        }
        int [] p = new int[2];
        p[0] = x;
        p[1] = y;
        
        return p;
    }
    
    private int[] convertToZone3(int X, int Y, int zone){
        int x;
        int y;
        if (zone == 1){
            x = -Y;
            y = X;
        }else if(zone == 2){
            x = -Y;
            y = -X;
        }else if(zone == 3){
            x = X;
            y = Y;
        }else if(zone == 4) {
            x = X;
            y = -Y;
        }else if(zone == 5){
            x = Y;
            y = -X;
        }else if (zone == 6){
            x = Y;
            y = X;
        }else if (zone == 7){
            x = -X;
            y = -Y;
        }else {
            x = -X;
            y = Y;
        }
        int [] p = new int[2];
        p[0] = x;
        p[1] = y;
        
        return p;
    }
    
    
    private int[] convertToZone4(int X, int Y, int zone){
        int x;
        int y;
        if (zone == 1){
            x = -Y;
            y = -X;
        }else if(zone == 2){
            x = -Y;
            y = X;
        }else if(zone == 3){
            x = X;
            y = -Y;
        }else if(zone == 4) {
            x = X;
            y = Y;
        }else if(zone == 5){
            x = Y;
            y = X;
        }else if (zone == 6){
            x = Y;
            y = -X;
        }else if (zone == 7){
            x = -X;
            y = Y;
        }else {
            x = -X;
            y = -Y;
        }
        int [] p = new int[2];
        p[0] = x;
        p[1] = y;
        
        return p;
    }
    
    private int[] convertToZone5(int X, int Y, int zone){
        int x;
        int y;
        if (zone == 1){
            x = -X;
            y = -Y;
        }else if(zone == 2){
            x = X;
            y = -Y;
        }else if(zone == 3){
            x = -Y;
            y = X;
        }else if(zone == 4) {
            x = Y;
            y = X;
        }else if(zone == 5){
            x = X;
            y = Y;
        }else if (zone == 6){
            x = -X;
            y = Y;
        }else if (zone == 7){
            x = Y;
            y = -X;
        }else {
            x = -Y;
            y = -X;
        }
        int [] p = new int[2];
        p[0] = x;
        p[1] = y;
        
        return p;
    }
    
    private int[] convertToZone6(int X, int Y, int zone){
        int x;
        int y;
        if (zone == 1){
            x = X;
            y = -Y;
        }else if(zone == 2){
            x = -X;
            y = -Y;
        }else if(zone == 3){
            x = Y;
            y = X;
        }else if(zone == 4) {
            x = -Y;
            y = X;
        }else if(zone == 5){
            x = -X;
            y = Y;
        }else if (zone == 6){
            x = X;
            y = Y;
        }else if (zone == 7){
            x = -Y;
            y = -X;
        }else {
            x = Y;
            y = -X;
        }
        int [] p = new int[2];
        p[0] = x;
        p[1] = y;
        
        return p;
    }
    
    private int[] convertToZone7(int X, int Y, int zone){
        int x;
        int y;
        if (zone == 1){
            x = Y;
            y = -X;
        }else if(zone == 2){
            x = Y;
            y = X;
        }else if(zone == 3){
            x = -X;
            y = -Y;
        }else if(zone == 4) {
            x = -X;
            y = Y;
        }else if(zone == 5){
            x = -Y;
            y = X;
        }else if (zone == 6){
            x = -Y;
            y = -X;
        }else if (zone == 7){
            x = X;
            y = Y;
        }else {
            x = X;
            y = -Y;
        }
        int [] p = new int[2];
        p[0] = x;
        p[1] = y;
        
        return p;
    }
    
    
    
    private void findAll8ZonePointAndDraw(GL2 gl, int x, int y, int xc, int yc) {
        int zone = findZone(x, y);
        
        int[] zone0 = convertToZone0(x, y, zone);
        int x0 = zone0[0];
        int y0 = zone0[1];
        Draw(gl, x0+xc, y0+yc);
        
        
        int[] zone1 = convertToZone1(x, y, zone);
        int x1 = zone1[0];
        int y1 = zone1[1];
        Draw(gl, x1+xc, y1+yc);
        
        
        int[] zone2 = convertToZone2(x, y, zone);
        int x2 = zone2[0];
        int y2 = zone2[1];
        Draw(gl, x2+xc, y2+yc);
        
        
        
        int[] zone3 = convertToZone3(x, y, zone);
        int x3 = zone3[0];
        int y3 = zone3[1];
        Draw(gl, x3+xc, y3+yc);
        
        int[] zone4 = convertToZone4(x, y, zone);
        int x4 = zone4[0];
        int y4 = zone4[1];
        Draw(gl, x4+xc, y4+yc);
        
        
        int[] zone5 = convertToZone5(x, y, zone);
        int x5 = zone5[0];
        int y5 = zone5[1];
        Draw(gl, x5+xc, y5+yc);
        
        
        int[] zone6 = convertToZone6(x, y, zone);
        int x6 = zone6[0];
        int y6 = zone6[1];
        Draw(gl, x6+xc, y6+yc);
        
         int[] zone7 = convertToZone7(x, y, zone);
        int x7 = zone7[0];
        int y7 = zone7[1];
        Draw(gl, x7+xc, y7+yc);
        
    }
    
    public void Draw(GL2 gl, int x, int y){
        gl.glColor3d(1, 0, 0);
        gl.glBegin(GL2.GL_POINTS);
        gl.glVertex2d(x, y);
        gl.glEnd();
    }
    

    public void reshape(GLAutoDrawable drawable, int x, int y, int width,
            int height) {
    }

    public void dispose(GLAutoDrawable arg0) {

    }

    public static void main(String[] args) {
        // TODO code application logic here
        //getting the capabilities object of GL2 profile
        final GLProfile profile = GLProfile.get(GLProfile.GL2);
        GLCapabilities capabilities = new GLCapabilities(profile);
        // The canvas
        final GLCanvas glcanvas = new GLCanvas(capabilities);
        task t = new task();
        glcanvas.addGLEventListener(t);
        glcanvas.setSize(600, 600);
        //creating frame
        final JFrame frame = new JFrame("Circle Drawing");
        //adding canvas to frame
        frame.add(glcanvas);
        frame.setSize(800, 480);
        frame.setVisible(true);
    }

}