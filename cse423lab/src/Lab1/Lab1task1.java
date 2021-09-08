package Lab1;

import com.jogamp.opengl.GL2;
import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.GLCapabilities;
import com.jogamp.opengl.GLEventListener;
import com.jogamp.opengl.GLProfile;
import com.jogamp.opengl.awt.GLCanvas;
import com.jogamp.opengl.glu.GLU;
import java.lang.Math;
import javax.swing.JFrame;
import java.util.Random;

public class Lab1task1 {

    public static void main(String args[]) {
        // getting the capabilities object of GL2 profile
        final GLProfile profile = GLProfile.get(GLProfile.GL2);
        GLCapabilities capabilities = new GLCapabilities(profile);
        // The canvas
        final GLCanvas glcanvas = new GLCanvas(capabilities);
       
        task1 t1 = new task1();
      
        glcanvas.addGLEventListener(t1);
        glcanvas.setSize(400, 400);
        // creating frame
        final JFrame frame = new JFrame("Draw 50 points");
        // adding canvas to frame
        frame.add(glcanvas);
        frame.setSize(1000, 480);
        frame.setVisible(true);
    }
}

class task1 implements GLEventListener {

    private GLU glu;

    public void init(GLAutoDrawable gld) {
        GL2 gl = gld.getGL().getGL2();
        glu = new GLU();

        gl.glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        gl.glViewport(-250, -150, 250, 150);
        gl.glMatrixMode(GL2.GL_PROJECTION);
        gl.glLoadIdentity();
        glu.gluOrtho2D(-300.0, 300.0, -300, 300.0);
    }

    public void display(GLAutoDrawable drawable) {
        GL2 gl = drawable.getGL().getGL2();
        
        draw50points(gl);

    }
    
     private void draw50points(GL2 gl){
        gl.glClear(GL2.GL_COLOR_BUFFER_BIT);
        gl.glColor3d(1, 0, 0);
        gl.glPointSize(2.0f);
        gl.glBegin(GL2.GL_POINTS);  
        Random rd = new Random();
        int lowerBound = 1;
        int upperBound = 51;
        for (int i = 0; i < 51; i++) {
            int x = rd.nextInt(upperBound);
            int y = rd.nextInt(upperBound);

            gl.glVertex2d(x, y);
        }
        gl.glEnd();
    }

    public void reshape(GLAutoDrawable drawable, int x, int y, int width, int height) {
    }

    public void displayChanged(GLAutoDrawable drawable, boolean modeChanged, boolean deviceChanged) {
    }

    public void dispose(GLAutoDrawable arg0) {

    }

}
