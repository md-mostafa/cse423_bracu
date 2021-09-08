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
import java.util.Scanner;

public class Lab1task3 {

    public static void main(String args[]) {
        // getting the capabilities object of GL2 profile
        final GLProfile profile = GLProfile.get(GLProfile.GL2);
        GLCapabilities capabilities = new GLCapabilities(profile);
        // The canvas
        final GLCanvas glcanvas = new GLCanvas(capabilities);
       
        task3 t3 = new task3();
        //glcanvas.addGLEventListener(b);
        glcanvas.addGLEventListener(t3);
        glcanvas.setSize(400, 400);
        // creating frame
        final JFrame frame = new JFrame("Draw T oR H");
        // adding canvas to frame
        frame.add(glcanvas);
        frame.setSize(1000, 480);
        frame.setVisible(true);
    }
}

class task3 implements GLEventListener {

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
        
        int x;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter id : ");
        x = sc.nextInt();
        
        if(x%2==0){
            drawTails(gl);
        }else{
            drawHeads(gl);
        }

    }
    
    private void drawHeads(GL2 gl){
        gl.glBegin(GL2.GL_POINTS);
        gl.glPointSize(3.0f);
        gl.glColor3d(1, 0, 0);
        
        DDA(gl, -250, 0, -150, 0, true);    //horizontal dashed line
        DDA(gl, -250, 200, -250, -200, false);  //left vertical line
        DDA(gl, -150, 200, -150, -200, false);   //right vertical  line
        
        gl.glEnd();
    }

    private void drawTails(GL2 gl) {
        gl.glBegin(GL2.GL_POINTS);
        gl.glPointSize(3.0f);
        gl.glColor3d(1, 0, 0);

        DDA(gl, 150, 100, 150, -100, false); //vertical straight line
        DDA(gl, 80, 100, 230, 100, true);   //horizontal dashed line
        gl.glEnd();
    }

    private void DDA(GL2 gl, float x1, float y1, float x0, float y0, boolean d) {

        float dx = x1 - x0;
        float dy = y1 - y0;

        float steps = Math.abs(dx) > Math.abs(dy) ? Math.abs(dx) : Math.abs(dy);

        float xinc = dx / (float) steps;
        float yinc = dy / (float) steps;

        float x = x0;
        float y = y0;
        
        if(d){
            for(int i = 0; i<=steps; i++){
                gl.glPointSize(15.0f);
                gl.glColor3d(0, 1, 0);
                if (i % 5 == 0) {
                    gl.glVertex2d((float) x, (float) y);
                }
                x += xinc;
                y += yinc;
            }
        }else{
            gl.glPointSize(3.0f);
            gl.glColor3d(1, 0, 0);
            for(int i =0; i<=steps; i++){
                gl.glVertex2d((float) x, (float) y);
                x += xinc;
                y += yinc;
            }
        }

        

    }

    public void reshape(GLAutoDrawable drawable, int x, int y, int width, int height) {
    }

    public void displayChanged(GLAutoDrawable drawable, boolean modeChanged, boolean deviceChanged) {
    }

    public void dispose(GLAutoDrawable arg0) {

    }

}
