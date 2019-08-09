//
//  ViewController.m
//  printCanOpenUrl
//
//  Created by chundong hu on 2019/8/9.
//  Copyright © 2019 chundong hu. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    NSMutableString* testAppString = [[NSMutableString alloc] initWithCapacity:100];
    int max = 100;  
    for (int i = 1; i<= 100; i++) {
        NSString* schema = [NSString stringWithFormat:@"testApp%d",i];
        if ([[UIApplication sharedApplication] canOpenURL:[NSURL URLWithString:schema]] == NO) {
            [testAppString appendString:schema];
            max--;
        }
    }
    
    UILabel* label = [[UILabel alloc] initWithFrame:self.view.frame];
    [self.view addSubview:label];
    label.text = testAppString;
    label.numberOfLines = 0;
    label.font = [UIFont systemFontOfSize:12];
    label.textColor = [UIColor blackColor];
    NSLog(@"max = %d",max);
    
    // Do any additional setup after loading the view.
}


@end
